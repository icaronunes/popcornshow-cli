from datetime import datetime
from config import URL_BASE

def formatDate(date: str | None) -> datetime | None:
    if date == None: return date
    formatDate = date[:19]
    return datetime.strptime(formatDate, "%Y-%m-%dT%H:%M:%S")


def formatFullDate(date: str | None) -> datetime:
    if date == None: return "- -"
    return datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")


def createUrl(type: str, url: str) -> str:
    if (type == 'm'):
        return URL_BASE + 'movie' + '/' + url
    else:
        return URL_BASE + 'show' + '/' + url

def formatType(type: chr) -> str:
    if (type == 'm'):
        return 'Movie'
    elif type == 's':
        return 'Show'
    else:
        return '- -'


def formatSource(item: str) -> str:
    return item.replace('_', ' ').capitalize()


def formatSource(sources: list[str]) -> str:
    result = ""
    br = hasBr(sources.__len__())
    for (index, source) in enumerate(sources):
        result = result + " " + source.replace("_", " ").capitalize()
        result = result + applyBr(index, br)
    return result 

def hasBr(length: int):
    if length >= 4: return "\n" 
    else: return " "

def applyBr(index: int, br: str):
      if index > 0:
          return br
      else:
          return ""