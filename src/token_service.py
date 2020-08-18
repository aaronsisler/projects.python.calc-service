import json

import requests


class TokenService(object):
    o_auth_url = ""
    o_auth_token = ""
    bearer = ""
    o_auth_token_val = ""
    status_code = ""
    json_response = ""

    def __init__(self, o_auth_token):
        self.o_auth_url = "https://www.googleapis.com/oauth2/v3/tokeninfo"
        self.o_auth_token = o_auth_token
        try:
            self.bearer, self.o_auth_token_val = o_auth_token.split()
        except ValueError:
            raise Exception("Unauthorized")

        if self.bearer != "Bearer" or len(self.o_auth_token_val) < 10 or self.o_auth_url == "":
            raise Exception("Unauthorized")

    def validate_token(self):
        headers = {"Accept": "application/json"}

        response = requests.get(self.o_auth_url, params={"id_token": self.o_auth_token_val})
        print("Code", response.status_code)
        self.status_code = response.status_code

        if self.status_code != 200:
            raise Exception("Unauthorized")

        self.json_response = json.loads(response.text)

        return self.status_code, self.json_response
