from fastapi.testclient import TestClient

from rabbitmq_cqrs_poc.entrypoint.app import app


def test_stores_a_subject_in_subject_repository():
    client = TestClient(app)
    response = client.post("/subject", json={"id_": "test_id", "name": "test_name"})
    assert response.status_code == 201
