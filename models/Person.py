from typing import List, Optional
from datetime import datetime


class Person:
    id: int
    slug: str
    name: str
    birthdate: Optional[datetime]
    has_poster: bool
    has_square: bool
    role_type: int
    role: Optional[str]
    rank: Optional[int]

    def __init__(self, id: int, slug: str, name: str, birthdate: Optional[datetime], has_poster: bool, has_square: bool, role_type: int, role: Optional[str], rank: Optional[int]) -> None:
        self.id = id
        self.slug = slug
        self.name = name
        self.birthdate = birthdate
        self.has_poster = has_poster
        self.has_square = has_square
        self.role_type = role_type
        self.role = role
        self.rank = rank
