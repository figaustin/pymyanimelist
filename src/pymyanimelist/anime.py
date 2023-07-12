from _base import Base

class Anime(Base):
    
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.main_picture_medium = data["main_picture"]["medium"]
        self.alternative_titles = data["alternative_titles"]
    
    
            
        

    
    
        