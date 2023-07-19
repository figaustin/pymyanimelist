from typing import Optional
from dataclasses import dataclass

from pymyanimelist._base import Base


@dataclass
class RelatedAnimeNode():
    id: int
    title: str
    main_picture: dict

@dataclass
class RelatedAnime():
    node: RelatedAnimeNode
    relation_type: str
    relation_type_formatted: str

@dataclass
class Anime(Base):
    
    id: int
    title: str
    alternative_titles: Optional[dict]
    start_date: Optional[str]
    end_date: Optional[str]
    synopsis: Optional[str]
    mean: Optional[float]
    rank: Optional[int]
    popularity: Optional[int]
    num_list_users: Optional[int]
    num_scoring_users: Optional[int]
    nsfw: Optional[str]
    created_at: Optional[str]
    updated_at: Optional[str]
    media_type: Optional[str]
    status: Optional[str]
    genres: Optional[list[dict]]
    num_episodes: Optional[int]
    start_season: Optional[dict]
    broadcast: Optional[dict]
    source: Optional[str]
    average_episode_duration: Optional[int]
    rating: Optional[str]
    pictures: Optional[list[dict]]
    background: Optional[str]
    related_anime: Optional[list[RelatedAnime]]
    related_manga: Optional[list[dict]]
    recommendations: Optional[list[dict]]
    studios: Optional[list[dict]]
    statistics: Optional[dict]



    
    
            
        

    
    
        