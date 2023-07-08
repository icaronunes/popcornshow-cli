from popcorn.models.AlsoWatched import AlsoWatched
from popcorn.models.Rank import Rank


class Content:
    text: str
    ranks: list[Rank]
    also_watched: list[AlsoWatched]

    def __init__(
        self, text: str, ranks: list[Rank], also_watched: list[AlsoWatched]
    ) -> None:
        self.text = text
        self.ranks = ranks
        self.also_watched = also_watche
