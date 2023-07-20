import unittest
import os
from dotenv import load_dotenv
import requests

import pymyanimelist

class TestAnimeSearch(unittest.TestCase):

    def test_animesearch(self):
        load_dotenv()
        mal = pymyanimelist.MAL(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'))

        s = mal.search(search_type= "anime", search="akame")
        for i in s:
            print(i.title)

if __name__ == '__main__':
    unittest.main()
