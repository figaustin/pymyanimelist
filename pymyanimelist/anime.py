from typing import Optional
from dataclasses import dataclass

from ._base import Base

@dataclass
class Anime(Base):
    
    id: int
    title: str
    alternative_titles: dict
    start_date: str
    end_date: str
    synopsis: str
    mean: float
    rank: int
    popularity: int
    num_list_users: int
    num_scoring_users: int
    nsfw: str
    created_at: str
    updated_at: str
    media_type: str
    status: str
    genres: list[dict]
    num_episodes: int
    start_season: dict
    broadcast: dict
    source: str
    average_episode_duration: int
    rating: str
    pictures: list[dict]
    background: str
    related_anime: list[dict]
    related_manga: list[dict]
    recommendations: list[dict]
    studios: list[dict]
    statistics: dict


    
    
            
        

    
    
        