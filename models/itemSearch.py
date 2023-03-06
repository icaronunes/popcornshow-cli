from dataclasses import dataclass
from utils import createUrl as fullUrl, formatSource, formatType,formatDate


@dataclass
class ItemSearch():
    id: int
    title: str
    release: str
    type: str
    imdb: float
    online: list[str]
    url: str

    def formatLongType(self):
        return formatType(self.type)

    def formatOnline(self):
        return formatSource(self.online)

    def createUrl(self):
        return fullUrl(self.type, self.url)


    def formatSimpleDate(self):
        result = formatDate(self.release)
        if result == None: return "- -"
        return result.year
    
    def formatSimpleDateStr(self): 
        return str(self.formatSimpleDate())
    
    def imdbStr(self): return str(self.imdb)
