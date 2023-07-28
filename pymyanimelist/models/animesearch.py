from dataclasses import dataclass
from pymyanimelist._base import Base
from pymyanimelist.models.anime import Anime


@dataclass
class AnimeSearchNode:
    node: Anime

@dataclass
class AnimeSearch:
    data: list[AnimeSearchNode]


