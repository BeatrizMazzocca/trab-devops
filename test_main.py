# test_main.py

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_app_hello_world_status_code():
    response = client.get("/Hello world!")
    assert response.status_code == 200

def test_app_hello_world_message():
    response = client.get("/Hello world!")
    assert response.json() == {"message": "Hello World"}

def test_app_funcaotest_status_code():
    response = client.get("/funcaotest")
    assert response.status_code == 200

def test_app_funcaotest_message():
    response = client.get("/funcaotest")
    assert response.json() == {"teste": "Deu muito certo!"}

def test_invalid_path_returns_404():
    response = client.get("/invalid-path")
    assert response.status_code == 404
