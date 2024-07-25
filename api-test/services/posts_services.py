import requests
import json
import models.get_response_model
import models.post_response_model
import constants

url = constants.BASE_URL + "/posts"

def get_posts():
    response = requests.get(url)
    return response

def post_posts(payload):
    response = requests.post(url, json=payload)
    return response

