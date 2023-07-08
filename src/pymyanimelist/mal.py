import secrets
import requests
import json

from _base import Base


class MAL(Base):
    def __init__(self, client_id: str = None, client_secret: str = None):
        self._client_id = client_id
        self._client_secret = client_secret
        self.access_token = None
        self.__make_session()

    def __make_session(self):
        code_verifier= self.__get_new_code_verifier()
        self.__print_new_authorisation_url(code_challenge=code_verifier)

        auth_code = input(f'Copy-paste the Auth code: ').strip()
        token = self.__generate_new_token(auth_code, code_verifier)

        self.print_user_info()

    def __new_code_verifier(self) -> str:
        token = secrets.token_urlsafe(100)
        return token[:128]
    
    def new_authorization_url(self):
        code_verifier= self.__new_code_verifier()
        url = f'https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={self._client_id}&code_challenge={code_verifier}'
        return url
    
    def generate_new_token(self, auth_code: str, code_verifier: str) -> dict:

        url = 'https://myanimelist.net/v1/oauth2/token'
        data = {
            'client_id': self._client_id,
            'client_secret': self._client_secret,
            'code': auth_code,
            'code_verifier': code_verifier,
            'grant_type': 'authorization_code'
        }

        response = requests.post(url, data)
        response.raise_for_status()  # Check whether the request contains errors

        token = response.json()
        response.close()
        print('Token generated successfully!')

        # with open('token.json', 'w') as file:
        #     json.dump(token, file, indent = 4)
        #     print('Token saved in "token.json"')
        self.access_token = token['access_token']

        return token
    
    def print_user_info(self):
        url = 'https://api.myanimelist.net/v2/users/@me'
        response = requests.get(url, headers = {
            'Authorization': f'Bearer {self.access_token}'
            })
        
        response.raise_for_status()
        user = response.json()
        response.close()

        print(f"\n>>> Greetings {user['name']}! <<<")








        
