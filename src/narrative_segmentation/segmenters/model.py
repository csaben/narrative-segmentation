from __future__ import annotations


class Segmenter:
    def segment(self, text: str, max_segment_length: int) -> list(str):  # type: ignore
        """Segment body of text with provided Segmenter.

        goals:
            1. split text into sentences
            2. include as many sentences as possible
            3. should pop >=1 sentence based on max length + semantic continuity

        Example:
            segmenter = SegmenterClass()
            segments = segmenter.segment(text, max_seg_len)
        """
        raise NotImplementedError
