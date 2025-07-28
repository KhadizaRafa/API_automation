import requests
import json

class Service:
    def __init__(self, url, method, body=None, token=None):
        self.url = url
        self.method = method.upper()
        self.body = body
        self.token = token
        self.header = {'Content-Type': 'application/json'}

        if self.token:
            self.header["Authorization"] = f"Bearer {self.token}"

    def get_request(self):
        response = requests.get(self.url, headers=self.header)
        return response

    def post_request(self):
        response=requests.post(self.url, headers=self.header, json=self.body)
        return response

