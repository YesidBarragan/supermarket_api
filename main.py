from db.client_db import ClientInDB
from db.client_db import update_client, get_client, database_clients

from models.client_models import ClientSearch, ClientIn, ClientOut

import datetime

from fastapi import FastAPI, HTTPException

api = FastAPI()

#Consultar Cliente
@api.get("/client/search/")
async def search_client(client_search: ClientSearch):
    client_in_db = get_client(client_search.cedula)
    if client_in_db == None:
        raise HTTPException(status_code=404, detail="El cliente no existe")
    if client_in_db.cedula == client_search.cedula:
        return client_in_db

#Actualizar Cliente
@api.post("/client/update/")
async def search_client(client_in_db: ClientInDB):
    database_clients.update({client_in_db.cedula:client_in_db})
    return database_clients[client_in_db.cedula]

#Agregar Cliente
@api.post("/client/new/")
async def update_client(client_in_db: ClientInDB):
    database_clients[client_in_db.cedula]=client_in_db
    return database_clients[client_in_db.cedula]