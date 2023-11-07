import json

import pytest
import requests
import jsonschema

from utils import load_schema


def regres_get(*args, **kwargs):
    url = kwargs.pop("url",'')
    return requests.get("https://reqres.in" + url, *args, **kwargs)


def test_get_users_status_code_is_ok():
    # response = requests.get(url="https://reqres.in/api/users")
    response = regres_get("/api/users")
    # print(response.text)
    assert response.status_code == 200


def test_get_users_per_page():
    response = requests.get(url="https://reqres.in/api/users", params={"per_page": 1})

    assert response.status_code == 200
    assert len(response.json()["data"]) == 1
    print(response.text)
    assert (response.json()["per_page"]) == 1

# @pytest.fixture
# def session():
#     bearer = {"Autorization": "Bearer qwrgt4erfw"}
#     headers = {"Connection": "keep-alive"}
#     session = Session()
#     session.headers = headers
#     return session
# def test_hearders(bearer, session):
#     response = session.get(url="https://reqres.in/api/users")
#     assert response.headers.get("connection") == "keep-alive"
#     assert response.status_code == 200

    # response = session.get(url="https://reqres.in/api/users", headers=headers)
    # response = requests.get(url="https://reqres.in/api/users", headers={"Accept": "*/*"})
    # headers = {"Connection": "keep-alive"}

    # return

    # headers.update(bearer)

def test_hearders():
    bearer = {"Autorization": "Bearer qwrgt4erfw"}
    headers = {"Connection": "keep-alive"}

    headers.update(bearer)
    response = requests.get(url="https://reqres.in/api/users", headers=headers)
    assert response.headers.get("connection") == "keep-alive"
    assert response.status_code == 200


def test_post_users_schema_validation():
    schema = load_schema("post_user.json")

    response = requests.post(
        url="https://reqres.in/api/users",
        json={
            "name": "Alex",
            "job": "QA"
        }
    )

    assert response.status_code == 201
    # assert response.json()['name'] == "Alex"
    jsonschema.validate(response.json(), schema)
