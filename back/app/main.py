from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth.auth import router
from config.config import settings
from routes.users import users_routes

app = FastAPI()

origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(  # parametros pra liberar a conexao
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_routes, tags=["Users"], prefix="/api/users")
app.include_router(router, tags=["Auth"], prefix="/api/auth")


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI with MongoDB"}
