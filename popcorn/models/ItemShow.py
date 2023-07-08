from datetime import datetime
from typing import Any
from popcorn.utils import createUrl as fullUrl, formatTrailers, filterTrailerByService, formatDate
from popcorn.tables.TableInterface import TableInterface
from popcorn.models.Seasons import Season
from popcorn.models.Person import Person
from popcorn.models.SourceAdPlacement import SourceAdPlacement
from popcorn.models.ScoreBreakdown import ScoreBreakdown
from popcorn.models.Tag import Tag
from popcorn.models.ReelgoodScores import ReelgoodScores
from popcorn.models.RegionalAvailability import RegionalAvailability
from popcorn.models.Metadata import Metadata
from popcorn.models.Trailer import Trailer
from popcorn.models.TVShowEpisode import TVShowEpisode
from dataclasses import dataclass


@dataclass
class Android:
    episode_id: str

    @staticmethod
    def from_dict(obj: Any) -> 'Android':
        _episode_id = str(obj.get("episode_id"))
        return Android(_episode_id)


@dataclass
class Ios:
    episode_id: str

    @staticmethod
    def from_dict(obj: Any) -> 'Ios':
        _episode_id = str(obj.get("episode_id"))
        return Ios(_episode_id)


@dataclass
class Links:
    web: str
    ios: str
    android: str

    @staticmethod
    def from_dict(obj: Any) -> 'Links':
        _web = str(obj.get("web"))
        _ios = str(obj.get("ios"))
        _android = str(obj.get("android"))
        return Links(_web, _ios, _android)


@dataclass
class References:
    # web: Web
    ios: Ios
    android: Android
    # webos: Webos

    @staticmethod
    def from_dict(obj: Any) -> 'References':
        _web = Web.from_dict(obj.get("web"))
        _ios = Ios.from_dict(obj.get("ios"))
        _android = Android.from_dict(obj.get("android"))
        _webos = Webos.from_dict(obj.get("webos"))
        return References(_web, _ios, _android, _webos)


@dataclass
class SourceData:
    links: Links
    references: References
    web_link: str

    @staticmethod
    def from_dict(obj: Any) -> 'SourceData':
        _links = Links.from_dict(obj.get("links"))
        _references = References.from_dict(obj.get("references"))
        _web_link = str(obj.get("web_link"))
        return SourceData(_links, _references, _web_link)


@dataclass
class Web:
    episode_id: str

    @staticmethod
    def from_dict(obj: Any) -> 'Web':
        _episode_id = str(obj.get("episode_id"))
        return Web(_episode_id)


@dataclass
class Webos:
    episode_id: str

    @staticmethod
    def from_dict(obj: Any) -> 'Webos':
        _episode_id = str(obj.get("episode_id"))
        return Webos(_episode_id)


@dataclass
class Recommended_episode:
    episode_id: str
    season_id: str


class ItemShow(TableInterface):
    metadata: Metadata
    id: str
    slug: str
    title: str
    overview: str
    reelgood_synopsis: str
    trailer: Trailer
    trailers: list[Trailer]
    imdb_rating: float
    rt_critics_rating: None
    rt_audience_rating: int
    has_poster: bool
    has_backdrop: bool
    season_count = int
    classification: str
    last_modified_at: datetime
    sources: list[str]
    released_on: datetime
    user_rating: None
    seen: bool
    user_lists: None
    on_free: bool
    on_rent_purchase: bool
    genres: list[int]
    tags: list[Tag]
    countries: list[str]
    tracking = bool
    people: list[Person]
    completed_on = bool
    score_breakdown: ScoreBreakdown
    regional_availability: RegionalAvailability
    reelgood_score = ReelgoodScores
    returning_on = str
    source_ad_placement: SourceAdPlacement
    source_ad_placements: list[SourceAdPlacement]
    unwatched = int
    coming_on = str
    has_new = bool
    recommended_episode = list[Recommended_episode]
    seasons = list[Season]
    episodes = list[TVShowEpisode]

    def __init__(self,  metadata: Metadata, id: str, slug: str, title: str, overview: str, reelgood_synopsis: str, classification: str, released_on: datetime, trailer: Trailer, trailers: list[Trailer], has_poster: bool, has_backdrop: bool, imdb_rating: float, rt_critics_rating: None, rt_audience_rating: int, last_modified_at: datetime, user_rating: None, user_lists: None, sources: list[str], on_free: bool, on_rent_purchase: bool, genres: list[int], tags: list[Tag], countries: list[str], people: list[Person], score_breakdown: ScoreBreakdown, reelgood_scores: ReelgoodScores, regional_availability: RegionalAvailability, source_ad_placement: SourceAdPlacement, source_ad_placements: list[SourceAdPlacement], season_count: int, tracking: bool, completed_on: bool, returning_on: str, unwatched: int, coming_on: str, has_new: bool, recommended_episode: list[Recommended_episode], imdb_votes: int, seasons: list[Season], episodes: list[TVShowEpisode], episode_availability: list[any], rating_stats: any = {}, reviews_count: int = 0) -> None:
        self.metadata = metadata
        self.id = id
        self.slug = slug
        self.title = title
        self.overview = overview
        self.tags = tags
        self.reelgood_synopsis = reelgood_synopsis
        self.classification = classification
        self.released_on = released_on
        self.tags = tags
        self.trailer = trailer
        self.trailers = trailers
        self.has_poster = has_poster
        self.has_backdrop = has_backdrop
        self.imdb_rating = imdb_rating
        self.rt_audience_rating = rt_audience_rating
        self.rt_critics_rating = rt_critics_rating
        self.last_modified_at = last_modified_at
        self.user_rating = user_rating
        self.user_lists = user_lists
        self.sources = sources
        self.on_free = on_free
        self.on_rent_purchase = on_rent_purchase
        self.genres = genres
        self.countries = countries
        self.people = people
        self.score_breakdown = score_breakdown
        self.regional_availability = regional_availability
        self.source_ad_placement = source_ad_placement
        self.source_ad_placements = source_ad_placements
        self.reelgood_score = reelgood_scores
        self.season_count = season_count
        self.tracking = tracking
        self.completed_on = completed_on
        self.returning_on = returning_on
        self.unwatched = unwatched
        self.coming_on = coming_on
        self.has_new = has_new
        self.recommended_episode = recommended_episode
        self.seasons = seasons
        self.episodes = episodes
        self.rating_stats = rating_stats
        self.reviews_count = reviews_count

    def get_number_seasons(self): return str(self.season_count)

    def createUrl(self):
        return fullUrl('s', self.slug)

    def get_overview(self):
        return self.overview

    def get_date(self) -> str:
        return self.formatDate()

    def get_time(self) -> str:
        return '-- --'

    def get_imdb(self) -> str:
        return str(self.imdb_rating)

    def get_classification(self) -> str:
        return f"[b][white]{self.classification}" if self.classification else 'Who knows?'

    def get_trailers(self) -> str:
        return self.getListTrailers()

    def getListTrailers(self) -> str:
        if self.trailer is not None:
            self.trailers.append(self.trailer)
            return formatTrailers(filterTrailerByService(self.trailers))
        else:
            search = self.slug.replace('-', '+')
            return f"[bold blue][link=https://www.youtube.com/results?search_query={search}]Search Youtube[/link]"

    def formatDate(self) -> str:
        return str(formatDate(self.released_on).date()) if self.released_on is not None else '-- --'
