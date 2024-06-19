from fastapi import APIRouter, Depends, HTTPException
from database.proyectos_DB import proyectos
from models.models import Proyecto
from security.security import *

router = APIRouter()

"""@router.get("/")
def read_root():
    return {"Hello": "World"}"""

@router.get("/proyecto", dependencies=[Depends(get_api_key)])
def leer_Proyecto() -> dict[str, dict[int, Proyecto]]:
    return {"proyecto": proyectos}

@router.get("/proyecto/{id}", dependencies=[Depends(get_api_key)])
def proyecto_Id(id: int) -> Proyecto:
    if id not in proyectos:
        raise HTTPException(
            status_code=404, detail=f"Proeycto con {id= } no existe."
        )
    return proyectos [id]

@router.put("/proyecto", dependencies=[Depends(get_api_key)])
def modificar_Proyecto(proyecto: Proyecto) -> dict[str, Proyecto]:
    if proyecto.id in proyectos:
        proyectos[proyecto.id] = proyecto
        return {"modificado": proyecto}
    
    raise HTTPException(
            status_code=400, detail=f"Proyecto con id: {proyecto.id } no existe."
        )
    
@router.post("/proyecto", dependencies=[Depends(get_api_key)])
def crear_Proyecto(proyecto: Proyecto) -> dict[str, Proyecto]:
    if proyecto.id in proyectos:

        raise HTTPException(
            status_code=400, detail=f"Proyecto con id: {proyecto.id } ya existe."
        )
    proyectos[proyecto.id] = proyecto

    return {"insertado": proyecto}