# workflow: backend made in src/folders , backend tested with api.py + shift-enter to use ipykernel
from __future__ import annotations

from narrative_segmentation.segmenters.model import Segmenter


def text_to_segments(segmenter_class: Segmenter, text: str, max_segment_length: int = 0) -> list(str):  # type: ignore  # noqa: E501
    """Consume a body of text and generate reasonable narrative chunks.

    Implementations:
        1 - naive sentence segmenter (as many sentences as possible
            that fit in model limit)
        2 - a model that can prune semantically unrelated sentences
            / narratively disjoint sentences move to next segment

    Assumptions:
        - TTS model we feed segments into cannot be conditioned on previous sentence
        (otherwise this would simply be a as many sentences as possible problem)

    """
    segmenter = segmenter_class()
    return segmenter.segment(text, max_segment_length)


if __name__ == "__main__":
    from narrative_segmentation.segmenters.naive import NaiveSegmenter

    text = "This is a test! Is this working? Yes... This is working. And this has no punctuation"
    segs = text_to_segments(NaiveSegmenter, text, 30)
    print(segs)
