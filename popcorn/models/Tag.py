class Tag:
    slug: str
    display_name: str

    def __init__(self, slug: str, display_name: str) -> None:
        self.slug = slug
        self.display_name = display_name
