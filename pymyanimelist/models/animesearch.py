from typing import Optional

from pymyanimelist._base import Base
from pymyanimelist.models.anime import Anime
from pymyanimelist.utils import as_dataclass


class AnimeSearch(Base):

    def __init__(self, data):
        self.results = self._format_search(data["data"])
        

    def _format_search(self, data) -> list[Anime]:
        """Cleans up the API response for ease of use."""

        new_arr = []
        for i in data:
            val = i["node"]
            new_arr.append(as_dataclass(Anime, val))
        return new_arr
        



