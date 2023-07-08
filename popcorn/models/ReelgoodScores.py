

class ReelgoodScores:
    streamability: float
    content: float
    follow_through: None
    reelgood_rank: int
    reelgood_popularity: float

    def __init__(self, streamability: float, content: float, follow_through: None, reelgood_rank: int, reelgood_popularity: float) -> None:
        self.streamability = streamability
        self.content = content
        self.follow_through = follow_through
        self.reelgood_rank = reelgood_rank
        self.reelgood_popularity = reelgood_popularity
