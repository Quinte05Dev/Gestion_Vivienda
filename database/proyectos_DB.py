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

proyectos = {
    0: Proyecto(id=0, tipo="Residencial", responsables="Andres", nombre="Robles", ubicacion="Manizales", estado="Construcción", descripcion=""),
    1: Proyecto(id=1, tipo="Comercial", responsables="Sebas", nombre="Cipres", ubicacion="Medellin", estado="Construcción", descripcion="120 mt2, cancha"),
    2: Proyecto(id=2, tipo="Residencial", responsables="Clau", nombre="Urapanes", ubicacion="Bogotá", estado="Terminada", descripcion="250 mt2, piscina"),
}