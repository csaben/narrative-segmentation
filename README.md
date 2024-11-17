# narrative-segmentation

create semantically continuous narrative chunks from a body of text

# Examples

## Basic segmenting based on provided max segment length

```python
from narrative_segmentation.segmenters.naive import NaiveSegmenter

text = "This is a test! Is this working? Yes... This is working. And this has no punctuation"
segs = text_to_segments(NaiveSegmenter, text, 30)
```

## Segmenting based on provided max segment length and semantic similiarity

```python
    from narrative_segmentation.segmenters.neural import NeuralSegmenter

    # Basic usage
    segmenter = NeuralSegmenter()
    text = (
        "First sentence about AI. Second sentence about AI. Third sentence about cats."
    )
    segments = segmenter.segment(
        text,
        100,
    )
    print(segments)

    # With auto-threshold adjustment to target number of segments
    segmenter.adjust_threshold(text, max_segment_length=100, target_segments=5)
```

# Limitations

A versatile implementation should actually attempt to identify narrative elements such as
dialogue sequences, speaker changes, or scene transitions.

As it stands neither `neural`, nor `naive` implementations do this.