import unittest
import os
from dotenv import load_dotenv
import requests

import pymyanimelist

class TestAnime(unittest.TestCase):

    def test_anime(self):
        load_dotenv()
        m = pymyanimelist.MAL(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'))
        
        with self.assertRaises(requests.HTTPError, msg="Test failed successfully, no errors occurred!"):
            anime = m.anime(1000)

if __name__ == '__main__':
    unittest.main()














