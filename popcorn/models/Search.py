from dataclasses import dataclass
from utils import createUrl as fullUrl, formatSources, formatType, formatDate


@dataclass
class Search():
    id: int
    title: str
    release: str
    type: str
    imdb: float
    online: list[str]
    slug: str

    def formatLongType(self):
        return formatType(self.type)

    def formatOnline(self):
        return formatSources(self.online)

    def createUrl(self):
        return fullUrl(self.type, self.slug)

    def formatSimpleDate(self):
        result = formatDate(self.release)
        if result == None:
            return "----"
        return result.year

    def formatSimpleDateStr(self):
        return str(self.formatSimpleDate())

    def imdbStr(self) -> str:
        if self.imdb != None:
            return str(self.imdb)
        else:
            return '-.-'
