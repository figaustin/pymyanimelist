from typing import Optional

from pymyanimelist._base import Base
from pymyanimelist.models.anime import Anime


class AnimeSearch(Base):

    def __init__(self, data):
        self.data = data["data"]
        

    def format_search(self) -> list[Anime]:
        new_arr = []
        for i in self.data:
            val = i["node"]
            new_arr.append(as_dataclass(Anime, val))
        return new_arr
        



