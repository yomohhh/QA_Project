import allure
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10

@allure.feature("API")
@allure.title("Get a single post returns 200 and the expected fields")
def test_get_post_returns_expected_structure():
    with allure.step("Send GET /posts/1"):
        response = requests.get(f"{BASE_URL}/posts/1", timeout=TIMEOUT)

    with allure.step("Check the status code is 200"):
        assert response.status_code == 200

    with allure.step("Check the response has the required fields"):
        data = response.json()
        assert set(data.keys()) == {"id", "userId", "title", "body"}

    with allure.step("Check the field values"):
        assert data["id"] == 1
        assert data["userId"] == 1


@allure.feature("API")
@allure.title("Get all users returns a list of 10 users")
def test_get_users_returns_list():
    with allure.step("Send GET /users"):
        response = requests.get(f"{BASE_URL}/users", timeout=TIMEOUT)

    with allure.step("Check the status code is 200"):
        assert response.status_code == 200

    with allure.step("Check the list contains 10 users with email"):
        users = response.json()
        assert isinstance(users, list)
        assert len(users) == 10
        assert all("email" in user for user in users)


@allure.feature("API")
@allure.title("Get a non-existing post returns 404")
def test_get_missing_post_returns_404():
    with allure.step("Send GET /posts/9999"):
        response = requests.get(f"{BASE_URL}/posts/9999", timeout=TIMEOUT)

    with allure.step("Check the status code is 404"):
        assert response.status_code == 404


@allure.feature("API")
@allure.title("Create a post returns 201 and echoes the sent data")
def test_create_post_returns_201():
    payload = {"title": "QA test", "body": "hello", "userId": 1}

    with allure.step("Send POST /posts with a new post"):
        response = requests.post(f"{BASE_URL}/posts", json=payload, timeout=TIMEOUT)

    with allure.step("Check the status code is 201"):
        assert response.status_code == 201

    with allure.step("Check the server returned the same data and an id"):
        data = response.json()
        assert data["title"] == payload["title"]
        assert data["userId"] == payload["userId"]
        assert "id" in data