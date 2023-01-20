from fastapi import FastAPI
from tranformacionesdedatos import dfAmazon
from tranformacionesdedatos import dfDisney
from tranformacionesdedatos import dfHulu
from tranformacionesdedatos import dfNetflix

import pandas as pd 


app =FastAPI(title='Datos disponibles de 4 plataformas de streaming',
             description= 'Puedes realizar 5 consultas determinas por cada una de las plataformas de streaming',
               )

@app.get("/")
def upload ():
    return "fabian"

@app.get("/palabraclave")
def read_root():
    
    return {"Hello": "fabian1"}

@app.get("/puntajemayor")
def read_root():
    return {"Hello": "fabian1"}

@app.get("/peliculaconmasapariciones")
def read_root():
    return {"Hello": "fabian1"}

@app.get("/peliculasporaño ")
def read_root():
    return {"Hello": "fabian1"}
