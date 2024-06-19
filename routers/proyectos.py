from fastapi import APIRouter
from database.proyectos_DB import *
from fastapi import HTTPException

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "World"}

@router.get("/proyecto")
def leer_Proyecto() -> dict[str, dict[int, Proyecto]]:
    return {"proyecto": proyectos}

@router.get("/proyecto/{id}")
def proyecto_Id(id: int) -> Proyecto:
    if id not in proyectos:
        raise HTTPException(
            status_code=404, detail=f"Proeycto con {id= } no existe."
        )
    return proyectos [id]

@router.post("/proyecto")
def crear_Proyecto(proyecto: Proyecto) -> dict[str, Proyecto]:
    if proyecto.id in proyectos:

        raise HTTPException(
            status_code=400, detail=f"Proyecto con id: {proyecto.id } ya existe."
        )
    proyectos[proyecto.id] = proyecto

    return {"insertado": proyecto}