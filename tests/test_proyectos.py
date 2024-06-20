import pytest
from fastapi.testclient import TestClient
from main import app
from models.models import Proyecto

client = TestClient(app)

fake_api_key = "Assessment_aprobado!!!"

headers = {
    "X-API-KEY": fake_api_key
}

def test_leer_proyecto():
    response = client.get("/proyecto", headers=headers)
    assert response.status_code == 200
    assert "proyecto" in response.json()

def test_proyecto_id_existente():
    response = client.get("/proyecto/1", headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_proyecto_id_no_existente():
    response = client.get("/proyecto/5", headers=headers)
    assert response.status_code == 404

def test_crear_proyecto():
    nuevo_proyecto = {
        "id": 3,
        "tipo": "Residencial",
        "responsables": "Edith",
        "nombre": "belen",
        "ubicacion": "Cartagena",
        "estado": "terminado",
        "descripcion": ""
    }
    response = client.post("/proyecto", json=nuevo_proyecto, headers=headers)
    assert response.status_code == 200
    assert response.json()["insertado"]["id"] == 3

def test_modificar_proyecto_existente():
    proyecto_modificado = {
        "id": 1,
        "tipo": "comercial",
        "responsables": "Sandra",
        "nombre": "Urapanes",
        "ubicacion": "Cali",
        "estado": "Terminada",
        "descripcion": "250 mt2, piscina"
    }
    response = client.put("/proyecto", json=proyecto_modificado, headers=headers)
    assert response.status_code == 200
    assert response.json()["modificado"]["id"] == 1
    assert response.json()["modificado"]["nombre"] == "Urapanes"

def test_modificar_proyecto_no_existente():
    proyecto_modificado = {
        "id": 5,
        "tipo": "Residencial",
        "responsables": "Luis",
        "nombre": "Inexistente",
        "ubicacion": "Bogotá",
        "estado": "Construcción",
        "descripcion": "Proyecto no existente"
    }
    response = client.put("/proyecto", json=proyecto_modificado, headers=headers)
    assert response.status_code == 400
    assert response.json()["detail"] == "Proyecto con id: 5 no existe."
