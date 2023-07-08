from typing import Optional
from dataclasses import dataclass
from popcorn.api.models.SearchApi import Item


@dataclass
class PersonApi:
    no_index: bool
    id: str
    slug: str
    name: str
    birthplace: str|None
    birthdate: Optional[str]
    deathdate: Optional[str]
    gender: str
    biography: str|None
    homepage: Optional[str]
    has_poster: bool
    has_square: bool
    initial_credits: list[Item]
