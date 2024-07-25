import pytest
import constants
from services.posts_services import get_posts, post_posts

url = constants.BASE_URL + "/posts"


def test_getapi():
    
    response = get_posts()
    assert response.status_code == 200

    data = response.json()
    
    for el in data:
        try: 
            assert isinstance(el["userId"], int)
            assert isinstance(el["id"], int)
            assert isinstance(el["title"], str)
            assert isinstance(el["body"], str)
        except AssertionError:
            print("Invalid data type on id " + str(el["id"]))
            raise AssertionError
    
    print("Get API Test Passed, all data types are valid")

    

test_getapi()

