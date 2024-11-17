from __future__ import annotations

from narrative_segmentation.segmenters.model import Segmenter


class NaiveSegmenter(Segmenter):
    def segment(self: Segmenter, text: str, max_segment_length: int) -> list(str):  # type: ignore
        return text.split(" .")
