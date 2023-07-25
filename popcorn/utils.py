from datetime import datetime

from popcorn.config import URL_BASE
from popcorn.models.Trailer import Trailer


def format_date(date: str | None) -> datetime | str | None:
    if date is None:
        return None
    try:
        formatDate = date[:19]
        return datetime.strptime(formatDate, "%Y-%m-%dT%H:%M:%S")
    except:
        return None


def format_date_str(date: str | None) -> str:
    if date is None:
        return "--"

    try:
        formatDate = date[:19]
        return str(datetime.strptime(formatDate, "%Y-%m-%dT%H:%M:%S").date())
    except:
        return "-- -- --"


def create_url(type: str, url: str) -> str:
    if type == "m":
        return URL_BASE + "movie" + "/" + url
    else:
        return URL_BASE + "show" + "/" + url


def format_type(type: chr) -> str:
    if type == "m":
        return "Movie"
    elif type == "s":
        return "Show"
    else:
        return "- -"


def format_source(item: str) -> str:
    return item.replace("_", " ").title()


def format_sources(sources: list[str]) -> str:
    result = ""
    br = has_br(sources.__len__())
    sources = remove_dash(sources=sources)
    for index, source in enumerate(sources):
        result = result + source + (br if index != sources.__len__() - 1 else "")
    return result


def remove_dash(sources: list[str]) -> list[str]:
    result = []
    for source in map(lambda x: x.replace("_", " ").capitalize(), sources):
        result.append(source)
    return result


def has_br(length: int):
    if length >= 15:
        return "\n"
    else:
        return " - "


def format_trailers(trailers: list[Trailer]) -> str:
    result = ""
    values = set(map(lambda x: x["key"], trailers))
    for index, value in enumerate(values):
        result = (
            result
            + f":link: [bold blue][link=https://youtu.be/{value}]Trailer - {index + 1}[/link][/bold blue]\n"
        )
    return result


def filterTrailerByService(trailers: list[Trailer], service="youtube") -> list[Trailer]:
    return filter(lambda x: x["site"] == service, trailers)
