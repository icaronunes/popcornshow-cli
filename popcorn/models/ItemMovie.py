from datetime import datetime
from typing import Optional

from popcorn.models.Ios import Ios
from popcorn.models.Links import Links
from popcorn.models.Metadata import Metadata
from popcorn.models.Person import Person
from popcorn.models.RatingStats import RatingStats
from popcorn.models.ReelgoodScores import ReelgoodScores
from popcorn.models.RegionalAvailability import RegionalAvailability
from popcorn.models.ScoreBreakdown import ScoreBreakdown
from popcorn.models.SourceAdPlacement import SourceAdPlacement
from popcorn.models.Tag import Tag
from popcorn.models.Trailer import Trailer
from popcorn.tables.TableInterface import TableInterface
from popcorn.utils import create_url as full_urls
from popcorn.utils import filterTrailerByService, format_date
from popcorn.utils import format_sources as format_sources_util
from popcorn.utils import format_trailers


class References:
    web: Ios
    ios: Ios
    android: Optional[Ios]
    webos: Optional[Ios]

    def __init__(
        self, web: Ios, ios: Ios, android: Optional[Ios], webos: Optional[Ios]
    ) -> None:
        self.web = web
        self.ios = ios
        self.android = android
        self.webos = webos


class SourceData:
    links: Links
    references: Optional[References]
    web_link: str

    def __init__(
        self, links: Links, references: Optional[References], web_link: str
    ) -> None:
        self.links = links
        self.references = references
        self.web_link = web_link


class Availability:
    rental_cost_hd: Optional[float | None]
    rental_cost_sd: Optional[float | None]
    purchase_cost_hd: Optional[float | None]
    purchase_cost_sd: Optional[float | None]
    source_id: str
    source_name: str
    access_type: int
    source_data: SourceData

    def __init__(
        self,
        rental_cost_hd: Optional[float | None],
        rental_cost_sd: Optional[float | None],
        purchase_cost_hd: Optional[float | None],
        purchase_cost_sd: Optional[float | None],
        source_id: str,
        source_name: str,
        access_type: int,
        source_data: SourceData,
    ) -> None:
        self.rental_cost_hd = rental_cost_hd
        self.rental_cost_sd = rental_cost_sd
        self.purchase_cost_hd = purchase_cost_hd
        self.purchase_cost_sd = purchase_cost_sd
        self.source_id = source_id
        self.source_name = source_name
        self.access_type = access_type
        self.source_data = source_data


class TextReasons:
    text: str


class ItemMovie(TableInterface):
    metadata: Metadata
    id: str
    slug: str
    title: str
    overview: str
    tagline: str
    reelgood_synopsis: str
    classification: str
    runtime: int
    released_on: datetime
    trailer: Trailer
    trailers: list[Trailer]
    language: str
    has_poster: bool
    has_backdrop: bool
    imdb_rating: float
    imdb_votes: int
    rt_critics_rating: None
    rt_audience_rating: int
    last_modified_at: datetime
    user_rating: None
    watchlisted: bool
    seen: bool
    user_lists: None
    sources: list[str]
    on_free: bool
    on_rent_purchase: bool
    genres: list[int]
    tags: list[Tag]
    countries: list[str]
    availability: list[Availability]
    people: list[Person]
    score_breakdown: ScoreBreakdown
    reelgood_scores: ReelgoodScores
    regional_availability: RegionalAvailability
    source_ad_placement: SourceAdPlacement
    source_ad_placements: list[SourceAdPlacement]
    rating_stats: RatingStats
    reviews_count: int
    madlib_synopsis: str
    where_to_wathc: str
    reasons_to_watch: list[TextReasons]

    def __init__(
        self,
        metadata: Metadata,
        id: str,
        slug: str,
        title: str,
        overview: str,
        tagline: str,
        reelgood_synopsis: str,
        classification: str,
        runtime: int,
        released_on: datetime,
        trailer: Trailer,
        trailers: list[Trailer],
        language: str,
        has_poster: bool,
        has_backdrop: bool,
        imdb_rating: float,
        imdb_votes: int,
        rt_critics_rating: None,
        rt_audience_rating: int,
        last_modified_at: datetime,
        user_rating: None,
        watchlisted: bool,
        seen: bool,
        user_lists: None,
        sources: list[str],
        on_free: bool,
        on_rent_purchase: bool,
        genres: list[int],
        tags: list[Tag],
        countries: list[str],
        availability: list[Availability],
        people: list[Person],
        score_breakdown: ScoreBreakdown,
        reelgood_scores: ReelgoodScores,
        regional_availability: RegionalAvailability,
        source_ad_placement: SourceAdPlacement,
        source_ad_placements: list[SourceAdPlacement],
        rating_stats: RatingStats,
        reviews_count: int = 0,
        madlib_synopsis: str = "",
        where_to_watch: str = "",
        reasons_to_watch: list[TextReasons] = [],
    ) -> None:
        self.metadata = metadata
        self.id = id
        self.slug = slug
        self.title = title
        self.overview = overview
        self.tagline = tagline
        self.reelgood_synopsis = reelgood_synopsis
        self.classification = classification
        self.runtime = runtime
        self.released_on = released_on
        self.trailer = trailer
        self.trailers = trailers
        self.language = language
        self.has_poster = has_poster
        self.has_backdrop = has_backdrop
        self.imdb_rating = imdb_rating
        self.imdb_votes = imdb_votes
        self.rt_critics_rating = rt_critics_rating
        self.rt_audience_rating = rt_audience_rating
        self.last_modified_at = last_modified_at
        self.user_rating = user_rating
        self.watchlisted = watchlisted
        self.seen = seen
        self.user_lists = user_lists
        self.sources = sources
        self.on_free = on_free
        self.on_rent_purchase = on_rent_purchase
        self.genres = genres
        self.tags = tags
        self.countries = countries
        self.availability = availability
        self.people = people
        self.score_breakdown = score_breakdown
        self.reelgood_scores = reelgood_scores
        self.regional_availability = regional_availability
        self.source_ad_placement = source_ad_placement
        self.source_ad_placements = source_ad_placements
        self.rating_stats = rating_stats
        self.reviews_count = reviews_count
        self.madlib_synopsis = madlib_synopsis
        self.where_to_watch = where_to_watch
        self.reasons_to_watch = reasons_to_watch

    def get_number_seasons(self):
        return "0"

    def get_overview(self):
        return self.overview

    def get_date(self) -> str:
        return self.format_date()

    def get_time(self) -> str:
        return self.format_time()

    def get_imdb(self) -> str:
        return self.imdb_str()

    def get_classification(self) -> str:
        return (
            f"[b][white]{self.classification}" if self.classification else "Who knows"
        )

    def get_trailers(self) -> str:
        return self.get_list_trailers()

    def format_date(self) -> str:
        return (
            str(format_date(self.released_on).date())
            if self.released_on is not None
            else "-- --"
        )

    def format_time(self) -> str:
        if self.runtime is not None:
            hours, minutes = divmod(self.runtime, 60)
            return f"{hours}h {minutes}m"
        else:
            return "-- --"

    def get_list_trailers(self) -> str:
        if self.trailer is not None:
            self.trailers.append(self.trailer)
            return format_trailers(filterTrailerByService(self.trailers))
        else:
            search = self.slug.replace("-", "+")
            return f"[bold blue][link=https://www.youtube.com/results?search_query={search}]Search Youtube[/link]"

    def format_sources(self) -> str:
        values = list(map(lambda x: x["source_name"], self.availability))
        return format_sources_util(values)

    def create_url(self):
        return full_urls("m", self.slug)

    def imdb_str(self) -> str:
        if self.imdb_rating != None:
            return str(self.imdb_rating)
        else:
            return "-.-"
