from typing import Union

from fastapi import FastAPI, HTTPException

from routers import proyectos

app = FastAPI()

app.include_router(proyectos.router)







