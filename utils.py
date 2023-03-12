from datetime import datetime
from config import URL_BASE
from models.Trailer import Trailer

BACK = 'back'


def formatDate(date: str | None) -> datetime | None:
    if date == None:
        return date
    formatDate = date[:19]
    return datetime.strptime(formatDate, "%Y-%m-%dT%H:%M:%S")


def formatFullDate(date: str | None) -> datetime:
    if date == None:
        return "- -"
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
    return item.replace('_', ' ').title()


def formatSources(sources: list[str]) -> str:
    result = ''
    br = __hasBr(sources.__len__())
    sources = remove_dash(sources=sources)
    for index, source in enumerate(sources):
        result = result + source + \
            (br if index != sources.__len__() - 1 else '')
    return result


def remove_dash(sources: list[str]) -> list[str]:
    result = []
    for source in map(lambda x: x.replace('_', ' ').capitalize(), sources):
        result.append(source)
    return result


def __hasBr(length: int):
    if length >= 15:
        return "\n"
    else:
        return " - "


def formatTrailers(trailers: list[Trailer]) -> str:
    result = ''
    values = set(map(lambda x: x['key'], trailers))
    for index, value in enumerate(values):
        result = result + \
            f"[bold blue][link=https://youtu.be/{value}]Trailer - {index + 1}[/link][/bold blue]\n"
    return result

def filterTrailerByService(trailers: list[Trailer], service='youtube') -> list[Trailer]:
    return filter(lambda x: x['site'] == service, trailers)
