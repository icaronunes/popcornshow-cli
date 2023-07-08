from models.Streamability import Streamability
from models.Content import Content

class ScoreBreakdown:
    streamability: list[Streamability]
    content: Content

    def __init__(self, streamability: list[Streamability], content: Content) -> None:
        self.streamability = streamability
        self.content = content