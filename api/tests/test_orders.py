import pytest
from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_read_orders():

    response = client.get("/orders/")

    assert response.status_code == 200
