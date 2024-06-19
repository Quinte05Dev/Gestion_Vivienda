from fastapi import FastAPI
from routers import proyectos

app = FastAPI()

app.include_router(proyectos.router)







