import requests

class Base:
    _MAL_URL = "https://api.myanimelist.net/v2"

        
    @property
    def _api_url(self) -> str:
            return self._MAL_URL

    def send_request(self, path: str, method: str = "GET", **kwargs) -> dict:
        url = f"{self._api_url}/{path}"
        client_id = kwargs.pop("client_id", None)
        headers = {"X-MAL-CLIENT-ID": client_id}
        body = kwargs.pop("body", None)
        params = kwargs.pop("params", None)
        with requests.request(method=method, url=url, params=params, data=body, headers=headers) as response:
             response.raise_for_status()
             data = response.json()
        
        return data
        