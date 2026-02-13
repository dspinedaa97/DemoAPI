from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() #Crear el objeto en FastAPI

#La API debe aceptar que estoy haciendo una petición en ese sitio
#CORS: Habilitar peticiones desde clientes que no están en mi dominio
    #Middleware se interpone entre el cliente y la APi

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.get("/sumar") # anotación de lo que va a ejecutar la API (en este caso: sumar)
def sumar_numeros(a:float, b:float):
    return a+b

@app.get("/restar")
def restar_numeros(a:float, b:float):
    return a-b