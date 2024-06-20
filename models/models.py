# Importamos BaseModel de la biblioteca Pydantic. Esto nos permite crear modelos de datos.
from pydantic import BaseModel
# Importamos Optional del módulo typing para definir atributos opcionales.
from typing import Optional

# Definimos la clase Proyecto con sus atributos y tipos de datos
class Proyecto(BaseModel):
    id: int
    tipo: str
    responsables: str
    nombre: str
    ubicacion: str
    estado: str
    descripcion: Optional[str]