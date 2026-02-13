from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() #Crear el objeto en FastAPI
@app.get("/sumar") # anotación de lo que va a ejecutar la API (en este caso: sumar)
def sumar_numeros(a:float, b:float):
    return a+b