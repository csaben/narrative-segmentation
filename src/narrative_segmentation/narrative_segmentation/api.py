from __future__ import annotations
from narrative_segmentation.narrative_segmentation.segmenters.model import Segmenter


def text_to_segments(segmenter: Segmenter, text:  str, max_segment_length: int = 0)  -> list(str): # type: ignore
    """
    summary: consume a body of text and generate reasonable narrative chunks

    implementations:
        1 - naive sentence segmenter (as many sentences as possible that fit in model limit)
        2 - a model that can prune semantically unrelated sentences / narratively disjoint sentences
        move to next segment

    assumptions:
        - TTS model we feed segments into cannot be conditioned on previous sentence (otherwise this would simply be a as
        many sentences as possible problem)

    """
    segmenter = Segmenter()
    return segmenter.segment(text, max_segment_length)