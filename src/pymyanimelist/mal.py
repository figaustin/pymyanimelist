import secrets
import requests
import json
from typing import Optional

from _base import Base
from anime import Anime


class MAL(Base):
    
    def __init__(self, client_id: str = None, client_secret: str = None):
        self._client_id = client_id
        self._client_secret = client_secret
        self.access_token = None
        self._code_verifier = None

    def __new_code_verifier(self) -> str:
        """Generates a new code verifier to be used for OAuth authentication"""
        token = secrets.token_urlsafe(100)
        return token[:128]
    
    def authenticate(self):

        """Generates a new MyAnimeList OAuth url. Redirect users to this url, to have them authorize your app with their MyAnimeList 
            Account, they will be redirected to the url you have setup in your MAL API app panel. Once they are redirected, you must
            catch the url the user is redirected to after and save the 'code' parameter's value.
        """
        self._code_verifier = self.__new_code_verifier()
        url = f'https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={self._client_id}&code_challenge={self._code_verifier}'
        return url
    
    def gen_auth_token(self, auth_code: str) -> str:

        """Generates a new token to use for accessing MAL API routes that have to do with a user's account.
        """

        if self._code_verifier is None:
            raise ValueError('Code verifier is null, use new_auth_url() first')

        url = 'https://myanimelist.net/v1/oauth2/token'
        data = {
            'client_id': self._client_id,
            'client_secret': self._client_secret,
            'code': auth_code,
            'code_verifier': self._code_verifier,
            'grant_type': 'authorization_code'
        }

        response = requests.post(url, data)
        response.raise_for_status()

        token = response.json()
        response.close()

        self.access_token = token['access_token']

        return token
    
    def anime(self, id: int):
        path = f"anime/{id}"
        data = self.send_request(path=path, method="GET", params={"fields": "title"}, client_id = self._client_id)
        return Anime(data=data)
        








        
