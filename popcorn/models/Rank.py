from popcorn.models.ListingKey import ListingKey


class Rank:
    rank: int
    text: str
    listing_key: ListingKey

    def __init__(self, rank: int, text: str, listing_key: ListingKey) -> None:
        self.rank = rank
        self.text = text
        self.listing_key = listing_key
