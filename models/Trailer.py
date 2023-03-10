
class Trailer:
    site: str
    key: str
    url: str | None

    def __init__(self, site: str, key: str, url: str) -> None:
        self.site = site
        self.key = key
        self.url = url
