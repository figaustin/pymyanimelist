import os
from typing import Optional
from requests import Session

class Base:
    MAL_URL = "https://api.myanimelist.net/v2/"

    def __init__(self, key: Optional[str] = None, session: Session = None):
        self._key = key if key is not None else os.environ.get("MAL_KEY")
        self._session = session

    @property
    def session(self) -> Session:
        return self._session

    @session.setter
    def session(self, session: Session) -> None:
        self._session = session

    @property
    def key(self) -> str:
        return self._key
    
    @key.setter
    def key(self, key: str) -> None:
        self._key = key

    @property
    def _host(self) -> str:
        return self.MAL_URL
    
    @property
    def _params(self) -> dict:
        return {
            "api_key": self.key,
        }
    
    def request(self, path: str, method: str = "GET", **kwargs) -> dict:
        url = f'{self._host}/{path}'
        json = kwargs.pop("json", None)
        params = {
            k.replace("__", "."): v
            for k, v in kwargs.items()
            if v is not None
        }
        params = {**self._params, **params}

        if self._session:
            if json is None:
                response = self.session.request(method, url, params=params)
            else:
                response = self.session.request(method, url, params=params, json=json)
            response.raise_for_status()
            data = response.json()
        else:
            with Session() as session:
                if json is None:
                    with session.request(method, url, params=params) as response:
                        response.raise_for_status()
                        data = response.json()
                else:
                    with session.request(method, url, params=params, json=json) as response:
                        response.raise_for_status()
                        data = response.json()

        
        return data