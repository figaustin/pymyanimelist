import unittest
import os
from dotenv import load_dotenv
import requests

import pymyanimelist

class TestMAL(unittest.TestCase):

    def test_mal(self):
        load_dotenv()
        mal = pymyanimelist.MAL(client_id="123123dd12", client_secret="ijnelkj2n3e")
        self.assertTrue(mal)

if __name__ == '__main__':
    unittest.main()