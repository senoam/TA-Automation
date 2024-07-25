import pytest
from services.posts_services import get_posts, post_posts


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
            print("Invalid data type on id " + str(el["id"]) + "\n")
            raise AssertionError
    
    print("Get API Test Passed, all data types are valid\n")

def test_postapi():

    # Payload variables initialization
    title = "recommendation"
    body = "motorcycle"
    userId = 12

    payload = {
        "title": title,
        "body": body,
        "userId": userId
    }

    response = post_posts(payload)
    assert response.status_code == 201

    data = response.json()

    try:
        assert isinstance(data["userId"], int)
        assert isinstance(data["id"], int)
        assert isinstance(data["title"], str)
        assert isinstance(data["body"], str)
        
        assert data["title"] == title
        assert data["body"] == body
        assert data["userId"] == 14

        assert len(data) > 0
    except AssertionError:
        print("POST API Test Failed, invalid data retrieved\n")
        raise AssertionError

    print("POST API Test Passed, all data types are valid\n")
