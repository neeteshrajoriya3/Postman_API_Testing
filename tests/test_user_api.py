import pytest
from utils.api_client import APIClient
import uuid

@pytest.fixture(scope="module")
def api_client():
    return APIClient()

def test_get_users(api_client):
    response = api_client.get("users")
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0
    print(response.json)

def test_create_users(api_client,load_user_data):
    # Hard coding the values for new user
    # user_data={
    #     "name" : "Prashant",
    #     "username": "qa user",
    #     "email": "test@gmail.com"
    # }
    user_data=load_user_data["new_user"]
    unique_email= f"{uuid.uuid4().hex[:8]}@gmail.com"
    user_data["username"]=unique_email
    response = api_client.post("users",user_data)
    print(response.json())

    assert response.status_code == 201
    assert response.json()["name"]==user_data["name"]
    assert response.json()["username"]==user_data["username"]
    assert response.json()["email"]==user_data["email"]
    print(response.json)

def test_update_users(api_client,load_user_data):
    # user_data={
    #     "name" : "Prashant1",
    #     "username": "qa user",
    #     "email": "test@gmail.com"
    # }
    user_data=load_user_data["update_user"]
    response = api_client.put("users/2",user_data)
    print(response.json())


