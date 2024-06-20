#import pytest
#from models.models import Proyecto

# TestClient nos permite hacer pruebas a nuestra aplicación FastAPI simulando peticiones HTTP.
from fastapi.testclient import TestClient
# Importamos la instancia de la aplicación FastAPI desde el archivo principal
from main import app

# Creamos un cliente de pruebas usando la aplicación FastAPI.
client = TestClient(app)

# Definimos una API-KEY falsa que usaremos para autenticar nuestras peticiones de prueba
fake_api_key = "Assessment_aprobado!!!"
# Creamos un diccionario de encabezados que incluye nuestra API-KEY.
headers = {
    "X-API-KEY": fake_api_key
}

# Función de prueba para verificar que se puede leer la lista de proyectos.
def test_leer_proyecto():
    # Hacemos una petición GET a la ruta /proyecto con los encabezados que incluyen el API-KEY.
    response = client.get("/proyecto", headers=headers)
    # Verificamos que el código de estado de la respuesta sea 200 (OK).
    assert response.status_code == 200
    # Verificamos que la respuesta JSON contenga el "proyecto".
    assert "proyecto" in response.json()

# Función de prueba para verificar que se puede leer un proyecto por su ID.
def test_proyecto_id_existente():
    response = client.get("/proyecto/1", headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == 1

# Función de prueba para verificar el comportamiento cuando el ID del proyecto no existe.
def test_proyecto_id_no_existente():
    response = client.get("/proyecto/5", headers=headers)
    assert response.status_code == 404

# Función de prueba para verificar que se puede crear un nuevo proyecto.
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

# Función de prueba para verificar que se puede modificar un proyecto existente.
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

# Función de prueba para verificar el comportamiento cuando se intenta modificar un proyecto que no existe.
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
