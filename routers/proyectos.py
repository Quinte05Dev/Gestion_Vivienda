# Importamos APIRouter que nos permite definir rutas de la API, Depends se usa para dependencias como la autenticación y HTTPException se usa para manejar errores.
from fastapi import APIRouter, Depends, HTTPException
# Importamos nuestra base de datos falsa, que contiene los datos de los proyectos.
from database.proyectos_DB import proyectos
# Importamos la clase Proyecto que define la estructura de los proyectos.
from models.models import Proyecto
# Importamos las funciones y configuraciones de seguridad desde el archivo security.py, incluyendo la verificación de la API-KEY.
from security.security import *

# Creamos una instancia de APIRouter para definir las rutas de la API.
router = APIRouter()

# Definimos una ruta GET para obtener todos los proyectos.
@router.get("/proyecto")
def leer_Proyecto() -> dict[str, dict[int, Proyecto]]:
    return {"proyecto": proyectos}

# Definimos una ruta GET para obtener un proyecto específico por su ID.
@router.get("/proyecto/{id}", dependencies=[Depends(get_api_key)]) # usamos la dependencia para que solo se pueda acceder al recurso con el API-KEY
# Definimos la función proyecto_Id que toma un parámetro id de tipo entero y retorna un objeto de tipo Proyecto
def proyecto_Id(id: int) -> Proyecto:
    # Verificamos si el id proporcionado no está en la base de datos proyectos.
    if id not in proyectos:
        # Si el id no está en la BD proyectos, lanzamos una excepción HTTP con el código de estado 404 (no encontrado) y un mensaje de detalle indicando que el proyecto con el id especificado no existe.
        raise HTTPException(
            status_code=404, detail=f"Proeycto con {id= } no existe."
        )
    # Si el id está en la BD proyectos, retornamos el proyecto correspondiente a ese id.
    return proyectos [id]

# Definimos una ruta PUT para actualizar un proyecto.
@router.put("/proyecto", dependencies=[Depends(get_api_key)])
def modificar_Proyecto(proyecto: Proyecto) -> dict[str, Proyecto]:
    if proyecto.id in proyectos:
        proyectos[proyecto.id] = proyecto
        return {"modificado": proyecto}
    raise HTTPException(
            status_code=400, detail=f"Proyecto con id: {proyecto.id } no existe."
        )

# Definimos una ruta POST para crear un nuevo proyecto.    
@router.post("/proyecto", dependencies=[Depends(get_api_key)])
def crear_Proyecto(proyecto: Proyecto) -> dict[str, Proyecto]:
    if proyecto.id in proyectos:
        raise HTTPException(
            status_code=400, detail=f"Proyecto con id: {proyecto.id } ya existe."
        )
    proyectos[proyecto.id] = proyecto

    return {"insertado": proyecto}