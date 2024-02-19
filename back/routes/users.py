from fastapi import APIRouter, HTTPException, Body, Depends
from bson import ObjectId

import models.model
from config.mongo_db import collection_user
from schemas.serializers import users_serializer, userResponseEntity
from models.model import User, Projects, UserResponseSchema

from auth.oauth2 import require_user

users_routes = APIRouter()


@users_routes.get("/")
async def get_users():
    users = users_serializer(collection_user.find())
    return {
        "status": "200",
        "data": users
    }


@users_routes.get("/{id}")
async def get_user(_id: str):
    user = users_serializer(collection_user.find({"_id": ObjectId(_id)}))
    return {
        "status": "200",
        "data": user
    }


@users_routes.post("/")
async def post_user(user: User = Body(...)):
    user_dict = user.dict()

    for index, project in enumerate(user_dict["projects"]):
        user_dict["projects"][index]["index"] = index + 1

    result = collection_user.insert_one(user_dict)

    if result.inserted_id:
        return {"message": "Usuário criado com sucesso", "user_id": str(result.inserted_id)}
    else:
        raise HTTPException(status_code=500, detail="Erro ao criar usuário no banco de dados")


# Projects ----------------------------

@users_routes.get("/{user_id}/projects")
async def get_all_projects_from_user(user_id: str):
    user = collection_user.find_one({"_id": ObjectId(user_id)})
    projects = user.get("projects", [])

    if user:
        return {
            "status": "okay",
            "data": projects
        }
    else:
        raise HTTPException(status_code=404, detail="User nao encontrado no banco")


@users_routes.get("/{user_id}/projects/{index}")
async def get_one_project_from_user(user_id: str, index: int):
    user = collection_user.find_one({"_id": ObjectId(user_id)})

    if user and index != 0:
        return {
            "status": "okay",
            "data": user["projects"][index]
        }
    elif index == 0:
        raise "Nao existe projeto com indice 0(zero), apenas maiores que 0(zero)"
    else:
        raise HTTPException(status_code=404, detail="User nao encontrado no banco")


@users_routes.post("/{user_id}/projects", description="Postar projeto em User especifico")
async def post_projects_in_user(user_id: str, project: Projects):
    user = users_serializer(collection_user.find({"_id": ObjectId(user_id)}))
    if user:
        project_dict = project.dict()
        index = len(user[0]["projects"])
        project_dict["index"] = index + 1
        result = collection_user.update_many(
            {"_id": ObjectId(user_id)},
            {"$addToSet": {"projects": project_dict}}
        )

        return {
            "status": "okay",
            "data": result
        }


@users_routes.get('/me', response_model=models.model.UserResponse)
def get_me(user_id: str = Depends(require_user())):
    user = userResponseEntity(collection_user.find_one({"_id": ObjectId(str(user_id))}))
    return {"status": "success", "user": user}
