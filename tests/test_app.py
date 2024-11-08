import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


def test_hello_world():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.data == b"Hello, World! This is a basic Flask app...."

def test_hello():
    with app.test_client() as client:
        response = client.get("/hello")
        assert response.status_code == 200
        assert response.data == b"Hello, no World!"