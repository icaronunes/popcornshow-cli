class AlsoWatched:
    id: int
    content_type: str
    slug: str
    title: str

    def __init__(self, id: int, content_type: str, slug: str, title: str) -> None:
        self.id = id
        self.content_type = content_type
        self.slug = slug
        self.title = title
