from fastapi.testclient import TestClient

from rabbitmq_cqrs_poc.entrypoint.app import app


def test_stores_a_subject():
    client = TestClient(app)
    response = client.post("/subject", json={"id_": "test_id", "name": "test_name"})
    assert response.status_code == 201


def test_retrieves_subjects():
    client = TestClient(app)
    response = client.get("/subjects")
    assert response.status_code == 200
    assert len(response.json()) == 3
