from typing import List

from bson import ObjectId
from pydantic import BaseModel, Field, BaseConfig


class OID(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            return ObjectId(str(v))
        except Exception:
            raise ValueError("not a valid ObjectId")


class MyBaseModel(BaseModel):
    def __hash__(self):
        return hash((type(self),) + tuple(self.__dict__.values()))


class Projects(MyBaseModel):
    title: str = Field(description='titulo', alias='title')
    imagePath: str = Field(description='caminho da image', alias='imagePath')
    url_project: str = Field(default='', description='caminho da image', alias='url')

    class Config(BaseConfig):
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: lambda oid: str(oid)
        }


class User(BaseModel):
    # id_user: ObjectId = Field(description='user id', alias='_id')
    name: str
    login: str
    projects: List[Projects] = Field(alias='projects')

    class Config(BaseConfig):
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: lambda oid: str(oid)
        }


class CreateUserSchema(User):
    password: str
    passwordConfirm: str
    verified: bool = False


class LoginUserSchema(BaseModel):
    name: str
    password: str


class UserResponseSchema(User):
    id: str
    pass


class UserResponse(BaseModel):
    status: str
    user: UserResponseSchema
