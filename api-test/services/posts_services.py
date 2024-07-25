import requests
import json
import constants

url = constants.BASE_URL + "/posts"

def get_posts():
    print("Calling GET on" + url)
    response = requests.get(url)
    return response

def post_posts(payload):
    print("\nCalling POST on " + url + " with payload: \n" + json.dumps(payload))
    
    response = requests.post(url, json=payload)

    print("\nResponse POST Data: \n" + str(response.json()) + "\n")
    return response

