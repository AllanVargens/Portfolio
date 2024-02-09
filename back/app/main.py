from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.model import Usuario
from routes.users import users_routes

app = FastAPI()

app.add_middleware( #parametros pra liberar a conexao
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_routes)

# @app.get("/")
# async def read_users() -> List[Usuario]:
#     users = [Usuario(**usuario) for usuario in collection.find()]
#     return users
#
# @app.get("/user/{id}")
# async def find_one(id: str):
#     user = collection.find_one({"_id": f"{id}"})
#     return user
