from dataclasses import dataclass
from datetime import datetime
from models.Trailer import Trailer
from typing import List, Optional
from uuid import UUID

from utils import formatDate, formatTrailers, formatSources, filterTrailerByService, createUrl as fullUrl


class Links:
    web: str
    ios: Optional[str]
    android: Optional[str]

    def __init__(self, web: str, ios: Optional[str], android: Optional[str]) -> None:
        self.web = web
        self.ios = ios
        self.android = android


class Ios:
    movie_id: str

    def __init__(self, movie_id: str) -> None:
        self.movie_id = movie_id


class References:
    web: Ios
    ios: Ios
    android: Optional[Ios]
    webos: Optional[Ios]

    def __init__(self, web: Ios, ios: Ios, android: Optional[Ios], webos: Optional[Ios]) -> None:
        self.web = web
        self.ios = ios
        self.android = android
        self.webos = webos


class SourceData:
    links: Links
    references: Optional[References]
    web_link: str

    def __init__(self, links: Links, references: Optional[References], web_link: str) -> None:
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

    def __init__(self, rental_cost_hd: Optional[float | None], rental_cost_sd: Optional[float | None], purchase_cost_hd: Optional[float | None], purchase_cost_sd: Optional[float | None], source_id: str, source_name: str, access_type: int, source_data: SourceData) -> None:
        self.rental_cost_hd = rental_cost_hd
        self.rental_cost_sd = rental_cost_sd
        self.purchase_cost_hd = purchase_cost_hd
        self.purchase_cost_sd = purchase_cost_sd
        self.source_id = source_id
        self.source_name = source_name
        self.access_type = access_type
        self.source_data = source_data


class Metadata:
    ad_data: None

    def __init__(self, ad_data: None) -> None:
        self.ad_data = ad_data


class Person:
    id: UUID
    slug: str
    name: str
    birthdate: Optional[datetime]
    has_poster: bool
    has_square: bool
    role_type: int
    role: Optional[str]
    rank: Optional[int]

    def __init__(self, id: UUID, slug: str, name: str, birthdate: Optional[datetime], has_poster: bool, has_square: bool, role_type: int, role: Optional[str], rank: Optional[int]) -> None:
        self.id = id
        self.slug = slug
        self.name = name
        self.birthdate = birthdate
        self.has_poster = has_poster
        self.has_square = has_square
        self.role_type = role_type
        self.role = role
        self.rank = rank


class ReelgoodScores:
    streamability: float
    content: float
    follow_through: None
    reelgood_rank: int
    reelgood_popularity: float

    def __init__(self, streamability: float, content: float, follow_through: None, reelgood_rank: int, reelgood_popularity: float) -> None:
        self.streamability = streamability
        self.content = content
        self.follow_through = follow_through
        self.reelgood_rank = reelgood_rank
        self.reelgood_popularity = reelgood_popularity


class RegionalAvailability:
    it: List[int]
    nl: List[int]
    de: List[int]
    fr: List[int]
    es: List[int]
    gb: List[int]
    au: List[int]
    us: List[int]

    def __init__(self, it: List[int], nl: List[int], de: List[int], fr: List[int], es: List[int], gb: List[int], au: List[int], us: List[int]) -> None:
        self.it = it
        self.nl = nl
        self.de = de
        self.fr = fr
        self.es = es
        self.gb = gb
        self.au = au
        self.us = us


class AlsoWatched:
    id: UUID
    content_type: str
    slug: str
    title: str

    def __init__(self, id: UUID, content_type: str, slug: str, title: str) -> None:
        self.id = id
        self.content_type = content_type
        self.slug = slug
        self.title = title


class ListingKey:
    listing_type: str
    listing_identifier: str

    def __init__(self, listing_type: str, listing_identifier: str) -> None:
        self.listing_type = listing_type
        self.listing_identifier = listing_identifier


class Rank:
    rank: int
    text: str
    listing_key: ListingKey

    def __init__(self, rank: int, text: str, listing_key: ListingKey) -> None:
        self.rank = rank
        self.text = text
        self.listing_key = listing_key


class Content:
    text: str
    ranks: List[Rank]
    also_watched: List[AlsoWatched]

    def __init__(self, text: str, ranks: List[Rank], also_watched: List[AlsoWatched]) -> None:
        self.text = text
        self.ranks = ranks
        self.also_watched = also_watched


class Streamability:
    type: str
    text: str

    def __init__(self, type: str, text: str) -> None:
        self.type = type
        self.text = text


class ScoreBreakdown:
    streamability: List[Streamability]
    content: Content

    def __init__(self, streamability: List[Streamability], content: Content) -> None:
        self.streamability = streamability
        self.content = content


class Creative:
    id: int
    campaign_name: str
    campaign_id: int
    advertiser_id: int
    ad_creative_type_id: int
    source_id: str
    image_override: None
    external_data: None
    links: None
    on_services: bool

    def __init__(self, id: int, campaign_name: str, campaign_id: int, advertiser_id: int, ad_creative_type_id: int, source_id: str, image_override: None, external_data: None, links: None, on_services: bool) -> None:
        self.id = id
        self.campaign_name = campaign_name
        self.campaign_id = campaign_id
        self.advertiser_id = advertiser_id
        self.ad_creative_type_id = ad_creative_type_id
        self.source_id = source_id
        self.image_override = image_override
        self.external_data = external_data
        self.links = links
        self.on_services = on_services


class SourceAdPlacement:
    placement_type: str
    source_id: str
    source_name: str
    access_type: int
    image_url: None
    title_copy: str
    short_deal_copy: str
    long_deal_copy: str
    additional_copy: None
    button_call_to_action: str
    landing_page_link: None
    use_deeplink: bool
    deeplink: str
    inline_position: str
    min_price: float
    creative: Creative
    links: Links

    def __init__(self, placement_type: str, source_id: str, source_name: str, access_type: int, image_url: None, title_copy: str, short_deal_copy: str, long_deal_copy: str, additional_copy: None, button_call_to_action: str, landing_page_link: None, use_deeplink: bool, deeplink: str, inline_position: str, min_price: float, creative: Creative, links: Links) -> None:
        self.placement_type = placement_type
        self.source_id = source_id
        self.source_name = source_name
        self.access_type = access_type
        self.image_url = image_url
        self.title_copy = title_copy
        self.short_deal_copy = short_deal_copy
        self.long_deal_copy = long_deal_copy
        self.additional_copy = additional_copy
        self.button_call_to_action = button_call_to_action
        self.landing_page_link = landing_page_link
        self.use_deeplink = use_deeplink
        self.deeplink = deeplink
        self.inline_position = inline_position
        self.min_price = min_price
        self.creative = creative
        self.links = links


class Tag:
    slug: str
    display_name: str

    def __init__(self, slug: str, display_name: str) -> None:
        self.slug = slug
        self.display_name = display_name


class ItemMovie:
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
    trailers: List[Trailer]
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
    sources: List[str]
    on_free: bool
    on_rent_purchase: bool
    genres: List[int]
    tags: List[Tag]
    countries: List[str]
    availability: List[Availability]
    people: List[Person]
    score_breakdown: ScoreBreakdown
    reelgood_scores: ReelgoodScores
    regional_availability: RegionalAvailability
    source_ad_placement: SourceAdPlacement
    source_ad_placements: List[SourceAdPlacement]

    def __init__(self, metadata: Metadata, id: UUID, slug: str, title: str, overview: str, tagline: str, reelgood_synopsis: str, classification: str, runtime: int, released_on: datetime, trailer: Trailer, trailers: List[Trailer], language: str, has_poster: bool, has_backdrop: bool, imdb_rating: float, imdb_votes: int, rt_critics_rating: None, rt_audience_rating: int, last_modified_at: datetime, user_rating: None, watchlisted: bool, seen: bool, user_lists: None, sources: List[str], on_free: bool, on_rent_purchase: bool, genres: List[int], tags: List[Tag], countries: List[str], availability: List[Availability], people: List[Person], score_breakdown: ScoreBreakdown, reelgood_scores: ReelgoodScores, regional_availability: RegionalAvailability, source_ad_placement: SourceAdPlacement, source_ad_placements: List[SourceAdPlacement]) -> None:
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

    def formatDate(self) -> str:
        return str(formatDate(self.released_on).date()) if self.released_on is not None else '-- --'

    def formatTime(self) -> str:
        if self.runtime is not None:
            hours, minutes = divmod(self.runtime, 60)
            return f'{hours}h {minutes}m'
        else:
            return '-- --'

    def getListTrailers(self) -> str:
        if self.trailer is not None:
            self.trailers.append(self.trailer)
        return formatTrailers(filterTrailerByService(self.trailers))

    def formatSources(self) -> str:
        values = list(map(lambda x: x['source_name'], self.availability))
        return formatSources(values)

    def createUrl(self):
        return fullUrl('m', self.slug)

    def imdbStr(self) -> str:
        if self.imdb_rating != None:
            return str(self.imdb_rating)
        else:
            return '-.-'
