from __future__ import annotations
from narrative_segmentation.narrative_segmentation.segmenters.model import Segmenter

class NaiveSegmenter(Segmenter):
    @staticmethod
    def segment(text: str, max_segment_length: int) -> list(str): # type: ignore
        sentences = text.split(" .")
        return sentences

