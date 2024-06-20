# APIKeyHeader nos permite manejar la autenticación basada en claves API (API Keys).
from fastapi.security.api_key import APIKeyHeader

from fastapi import HTTPException, Security
# HTTPException se usa para lanzar excepciones HTTP y Security se usa para implementar dependencias de seguridad en las  rutas.

# Definimos la instancia de APIKeyHeader
api_key_header = APIKeyHeader(name="X-API-KEY")

# API Key 
fake_api_key = "Assessment_aprobado!!!"

# Función para validar la API Key
def get_api_key(api_key: str = Security(api_key_header)):
    if api_key == fake_api_key:
        return api_key
    else:
        raise HTTPException(
            status_code=403,
            detail="Invalid API Key",
        )