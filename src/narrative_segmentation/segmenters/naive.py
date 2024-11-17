from __future__ import annotations

import re

from narrative_segmentation.segmenters.model import Segmenter


class NaiveSegmenter(Segmenter):
    def segment(self, text: str, max_segment_length: int) -> list[str]:
        if not isinstance(text, str):
            raise TypeError(f"Expected text to be str, got {type(text).__name__}")

        # Split on sentence endings (.!?...) followed by whitespace
        pattern = r"(?<=[.!?…])\s+"
        sentences = [s.strip() for s in re.split(pattern, text) if s.strip()]

        # Group sentences together up to max_segment_length
        segments = []
        current_segment = []
        current_length = 0

        for sentence in sentences:
            assert (
                len(sentence) <= max_segment_length
            ), f"A sentence exceeds max segment length: {sentence}"

            # Add ending punctuation if missing
            if not sentence[-1] in ".!?…":
                sentence += "."

            # Start new segment if this sentence would exceed length
            if current_length + len(sentence) > max_segment_length and current_segment:
                segments.append(" ".join(current_segment))
                current_segment = []
                current_length = 0

            current_segment.append(sentence)
            current_length += len(sentence) + 1  # +1 for space

        if current_segment:
            segments.append(" ".join(current_segment))

        return segments
