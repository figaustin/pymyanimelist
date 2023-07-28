from typing import Optional
from dataclasses import dataclass

from pymyanimelist._base import Base
from pymyanimelist.models.helper_models import (
    Picture,
    AlternativeTitle,
    Genre, 
    StartSeason,
    Broadcast,
)

@dataclass
class RelatedAnimeNode:
    id: int
    title: str
    main_picture: Picture

@dataclass
class RelatedAnime:
    node: RelatedAnimeNode
    relation_type: str
    relation_type_formatted: str

@dataclass
class Anime:
    
    id: int
    title: str
    main_picture: Optional[Picture]
    alternative_titles: Optional[AlternativeTitle]
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
    genres: Optional[list[Genre]]
    num_episodes: Optional[int]
    start_season: Optional[StartSeason]
    broadcast: Optional[Broadcast]
    source: Optional[str]
    average_episode_duration: Optional[int]
    rating: Optional[str]
    pictures: Optional[list[Picture]]
    background: Optional[str]
    related_anime: Optional[list[RelatedAnime]]
    related_manga: Optional[list[dict]]
    recommendations: Optional[list[dict]]
    studios: Optional[list[dict]]
    statistics: Optional[dict]



    
    
            
        

    
    
        