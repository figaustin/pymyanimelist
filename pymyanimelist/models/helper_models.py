from dataclasses import dataclass
from typing import Optional

@dataclass
class Picture:
    medium: Optional[str]
    large: Optional[str]

@dataclass
class AlternativeTitle:
    synonyms: Optional[list[str]]
    en: Optional[str]
    ja: Optional[str]

@dataclass
class Genre:
    id: Optional[int]
    name: Optional[str]

@dataclass
class StartSeason:
    year: Optional[int]
    season: Optional[str]

@dataclass
class Broadcast:
    day_of_the_week: Optional[str]
    start_time: Optional[str]