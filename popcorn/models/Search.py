from dataclasses import dataclass

from popcorn.utils import create_url as fullUrl
from popcorn.utils import format_date, format_sources, format_type


@dataclass
class Search:
    id: int
    title: str
    release: str
    type: str
    imdb: float
    online: list[str]
    slug: str

    def format_long_type(self):
        return format_type(self.type)

    def format_online(self):
        return format_sources(self.online)

    def create_url(self):
        return fullUrl(self.type, self.slug)

    def format_simple_date(self):
        result = format_date(self.release)
        if result == None:
            return "----"
        return result.year

    def format_simple_date_str(self):
        return str(self.format_simple_date())

    def imdb_str(self) -> str:
        if self.imdb != None:
            return str(self.imdb)
        else:
            return "-.-"
