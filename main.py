# Importa la clase FastAPI del módulo fastapi. Esta clase es usada para crear una instancia de la aplicación web.
from fastapi import FastAPI
# Importa el módulo proyectos desde la carpeta routers donde estan los endpoints.
from routers import proyectos

# Creamos una instancia de la aplicación FastAPI. Esta instancia es la que maneja todas las peticiones entrantes.
app = FastAPI()

# Esto nos permite que las rutas definidas en el archivo proyectos.py sean accesibles a través de la aplicación.
app.include_router(proyectos.router)







