from __future__ import annotations
from abc import ABC

class Segmenter(ABC):
    @staticmethod
    def segment(text: str, max_segment_length: int) -> list(str): # type: ignore
        """
        goals:
            1. split text into sentences
            2. include as many sentences as possible
            3. should pop >=1 sentence based on max length + semantic continuity

        example:
            segmenter = SegmenterClass()
            segments = segmenter.segment(text, max_seg_len)
        """
        raise NotImplementedError
