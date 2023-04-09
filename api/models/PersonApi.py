from typing import Optional
from dataclasses import dataclass
from api.models.SearchApi import Item


@dataclass
class PersonApi:
    no_index: bool
    id: str
    slug: str
    name: str
    birthplace: str
    birthdate: str
    deathdate: Optional[str]
    gender: str
    biography: str
    homepage: Optional[str]
    has_poster: bool
    has_square: bool
    initial_credits: list[Item]
