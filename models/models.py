from pydantic import BaseModel
from typing import Optional

class Proyecto(BaseModel):
    id: int
    tipo: str
    responsables: str
    nombre: str
    ubicacion: str
    estado: str
    descripcion: Optional[str]