
from _base import Base


class MAL(Base):
    def __init__(self, client_id: str = None, client_secret: str = None):
        super().__init__(client_id, client_secret)
        self.read_only = False if client_id is not None else True
    
    def anime(self, *argv):
        








        
