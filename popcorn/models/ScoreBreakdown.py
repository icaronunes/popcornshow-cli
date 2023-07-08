from popcorn.models.Content import Content
from popcorn.models.Streamability import Streamability


class ScoreBreakdown:
    streamability: list[Streamability]
    content: Content

    def __init__(self, streamability: list[Streamability], content: Content) -> None:
        self.streamability = streamability
        self.content = content
