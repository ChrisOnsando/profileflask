import pytest
from app import app as myapp
from app import db
import json

@pytest.fixture(scope="module")
def app():
    myapp.config.from_object("config.TestConfig")

    with myapp.app_context():
        db.create_all()
    
    yield myapp

@pytest.fixture
def client(app):
    client = app.test_client()
    yield client


def test_register(client):
    test_data = {
        "feedback": "Test feedback", 
        "username": "testusername",
        "email": "test@test.com",
        "password": "testpassword",
        "phonenumber": "07123456789"
    }

    response = client.post(
        "/register",
        data=json.dumps(test_data),
        content_type="application/json"
    )

    data = response.json
 
    assert response.status_code == 201
    assert data.get("message") == "User Account Successfully Created!"

def test_login(client):
    test_data = {
        "username": "testusername",
        "password": "testpassword"
    }

    response = client.post(
        "/login",
        data=json.dumps(test_data),
        content_type="application/json"
    )

    data = response.json
 
    assert response.status_code == 200

def test_update(client):
    data = {
        "feedback": "Test feedback", 
        "username": "testusername",
        "email": "test@test.com",
        "password": "testpassword",
        "phonenumber": "07123456789"
    }

    updated_data = {
        "feedback": "Test feedback", 
        "username": "testusername",
        "email": "test@test.com",
        "password": "testpassword",
        "phonenumber": "07123456789",
    }

    response = client.put(
        "/update",
        data=json.dumps(updated_data),
        content_type="application/json",
    )
    
    assert response.status_code == 200
    assert response.json["message"] == "User Details Updated Successfully!"
    