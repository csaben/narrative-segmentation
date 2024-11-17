import re
from typing import List

import numpy as np
from sentence_transformers import SentenceTransformer

from narrative_segmentation.segmenters.model import Segmenter


class NeuralSegmenter(Segmenter):
    def __init__(
        self, model_name: str = "all-MiniLM-L6-v2", similarity_threshold: float = 0.5
    ):
        """
        Initialize with a lightweight sentence transformer model.

        Args:
            model_name: Name of the sentence-transformers model to use
            similarity_threshold: Minimum cosine similarity to consider sentences related
        """
        self.model = SentenceTransformer(model_name)
        self.similarity_threshold = similarity_threshold

    def segment(self, text: str, max_segment_length: int) -> List[str]:
        if not isinstance(text, str):
            raise TypeError(f"Expected text to be str, got {type(text).__name__}")

        # Split into sentences
        pattern = r"(?<=[.!?…])\s+"
        sentences = [s.strip() for s in re.split(pattern, text) if s.strip()]

        # Add ending punctuation where missing
        sentences = [s + "." if not s[-1] in ".!?…" else s for s in sentences]

        # Get embeddings for all sentences
        embeddings = self.model.encode(sentences)

        # Calculate similarity matrix
        similarity_matrix = np.inner(embeddings, embeddings)

        # Group sentences based on similarity and length constraints
        segments = []
        current_segment = []
        current_length = 0

        for i, sentence in enumerate(sentences):
            # If this is the first sentence or if it's similar to previous sentences
            # and adding it wouldn't exceed length limit, add to current segment
            should_add = False

            if not current_segment:
                should_add = True
            else:
                # Check similarity with sentences in current segment
                current_indices = [sentences.index(s) for s in current_segment]
                similarities = [similarity_matrix[i][j] for j in current_indices]
                avg_similarity = np.mean(similarities)

                if avg_similarity >= self.similarity_threshold:
                    should_add = True

            if should_add and current_length + len(sentence) <= max_segment_length:
                current_segment.append(sentence)
                current_length += len(sentence) + 1
            else:
                if current_segment:
                    segments.append(" ".join(current_segment))
                current_segment = [sentence]
                current_length = len(sentence) + 1

        if current_segment:
            segments.append(" ".join(current_segment))

        return segments

    def adjust_threshold(
        self, text: str, max_segment_length: int, target_segments: int
    ) -> None:
        """
        Automatically adjust similarity threshold to achieve desired number of segments.
        """
        low, high = 0.0, 1.0
        while high - low > 0.01:
            mid = (low + high) / 2
            self.similarity_threshold = mid
            segments = self.segment(text, max_segment_length)

            if len(segments) > target_segments:
                high = mid
            else:
                low = mid
