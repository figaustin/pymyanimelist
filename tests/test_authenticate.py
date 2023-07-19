import unittest
import os
from dotenv import load_dotenv
import requests

import pymyanimelist

class TestAuthenticate(unittest.TestCase):

    def test_authenticate(self):
        """Tests user authentication by printing an auth url and asking for the code verifier from the callback url"""
        load_dotenv()
        mal = pymyanimelist.MAL(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'))
        print(mal.authenticate())
        auth_code = input("Enter Auth Code: ")

        with self.assertRaises(requests.HTTPError, msg="Test failed successfully, no errors occurred!"):
            mal.gen_auth_token(auth_code)
        

if __name__ == '__main__':
    unittest.main()