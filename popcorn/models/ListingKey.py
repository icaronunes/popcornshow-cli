class ListingKey:
    listing_type: str
    listing_identifier: str

    def __init__(self, listing_type: str, listing_identifier: str) -> None:
        self.listing_type = listing_type
        self.listing_identifier = listing_identifier
