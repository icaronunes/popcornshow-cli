from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, List, Optional

""""
    LIMPAR CLASSE
"""


class Classification(Enum):
    THE_13 = "13+"
    THE_16 = "16+"
    THE_18 = "18+"
    THE_7 = "7+"


class ContentType(Enum):
    def __str__(self) -> str:
        return self.name

    M = "m"
    S = "s"


@dataclass
class Item:
    id: str
    slug: str
    content_type: ContentType
    title: str
    overview: None
    availability_pros: None
    imdb_rating: Optional[float]
    rt_critics_rating: None
    rg_content_score: None
    has_poster: bool
    poster_blur: None
    has_backdrop: bool
    backdrop_blur: None
    released_on: Optional[datetime]
    classification: Optional[Classification]
    sources: List[str]
    genres: List[Any]
    on_services: bool
    on_free: bool
    on_rent_purchase: bool
    user_rating: None
    tracking: bool
    watchlisted: bool
    seen: bool
    season_count: int
    featured_services: List[Any]
    episode_source_count: int

    def __init__(
        self,
        id: str,
        slug: str,
        content_type: ContentType,
        title: str,
        overview: None,
        availability_pros: None,
        imdb_rating: Optional[float],
        rt_critics_rating: None,
        rg_content_score: None,
        has_poster: bool,
        poster_blur: None,
        has_backdrop: bool,
        backdrop_blur: None,
        released_on: Optional[datetime],
        classification: Optional[Classification],
        sources: List[str],
        genres: List[Any],
        on_services: bool,
        on_free: bool,
        on_rent_purchase: bool,
        user_rating: None,
        tracking: bool,
        watchlisted: bool,
        seen: bool,
        season_count: int,
        featured_services: List[Any],
        episode_source_count: int,
    ) -> None:
        self.id = id
        self.slug = slug
        self.content_type = content_type
        self.title = title
        self.overview = overview
        self.availability_pros = availability_pros
        self.imdb_rating = imdb_rating
        self.rt_critics_rating = rt_critics_rating
        self.rg_content_score = rg_content_score
        self.has_poster = has_poster
        self.poster_blur = poster_blur
        self.has_backdrop = has_backdrop
        self.backdrop_blur = backdrop_blur
        self.released_on = released_on
        self.classification = classification
        self.sources = sources
        self.genres = genres
        self.on_services = on_services
        self.on_free = on_free
        self.on_rent_purchase = on_rent_purchase
        self.user_rating = user_rating
        self.tracking = tracking
        self.watchlisted = watchlisted
        self.seen = seen
        self.season_count = season_count
        self.featured_services = featured_services
        self.episode_source_count = episode_source_count


@dataclass
class SearchApi:
    items: list[Item]
    page: int
    pages: int
    page_size: int

    #  FIZ PARA USAR LISTA
    def __init__(
        self, items: list[Item], page: int, pages: int, page_size: int
    ) -> None:
        print(items)
        self.items = items
        self.page = page
        self.pages = pages
        self.page_size = page_size
