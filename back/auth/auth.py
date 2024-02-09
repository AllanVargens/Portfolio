from datetime import datetime, timedelta
from bson.objectid import ObjectId
from fastapi import APIRouter, Response, status, Depends, HTTPException

from auth import oauth2
from config.mongo_db import collection_user
from schemas.serializers import user_serializer
from models import model
from utils import utils
from auth.oauth2 import AuthJWT
from config.config import settings


router = APIRouter()

ACCESS_TOKEN_EXPIRES_IN = settings.ACCESS_TOKEN_EXPIRES_IN
REFRESH_TOKEN_EXPIRES_IN = settings.REFRESH_TOKEN_EXPIRES_IN

@router.post('/register', status_code=status.HTTP_201_CREATED, response_model= model.UserResponse)
async def create_user(payload: model.CreateUserSchema):
    # Check if user already exist

    user = collection_user.find_one({'login': payload.login.lower()})
    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail= 'Account already exist')

    if payload.password != payload.passwordConfirm:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Passwords do not match")

    # Hash the password

    payload.password = utils.hash_password(payload.password)
    del payload.passwordConfirm

    payload.verified = True
    payload.login = payload.login.lower()
    payload.projects = []
    result = collection_user.insert_one(payload.dict())
    new_user = user_serializer(collection_user.find({'_id': result.inserted_id}))
    return {"status": "success", "user": new_user}


# LOGIN -------------------------------

@router.post("/login")
def login(payload: model.LoginUserSchema, response:Response, Authorize: AuthJWT = Depends()):
    # Check if the user exist
    db_user = collection_user.find_one({'login': payload.name.lower()})
    if not db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail= "Incorrect Login name or Password")

    user = user_serializer(db_user)

    # Check if the password is valid

    if not utils.verify_password(payload.password, user["password"]):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Incorrect Login name or Password")

    # Create access token
    access_token = Authorize.create_access_token(subject=str(user["_id"]), expires_time=timedelta(minutes=ACCESS_TOKEN_EXPIRES_IN))


    # Create refresh token
    refresh_token = Authorize.create_refresh_token(subject=str(user["_id"]), expires_time=timedelta(minutes=ACCESS_TOKEN_EXPIRES_IN))

    # Store refresh and access tokens in cookie

    response.set_cookie('access_token', access_token, ACCESS_TOKEN_EXPIRES_IN * 60,
                        ACCESS_TOKEN_EXPIRES_IN * 60, '/', None, False, True, 'lax')

    response.set_cookie("refresh_token", refresh_token,
                        REFRESH_TOKEN_EXPIRES_IN * 60, REFRESH_TOKEN_EXPIRES_IN * 60, '/', None, False, True, 'lax')

    response.set_cookie("logged_in", "True", ACCESS_TOKEN_EXPIRES_IN * 60,
                        ACCESS_TOKEN_EXPIRES_IN * 60, "/", None, False, False, "lax")

    # Send both access

    return {"status": "success", "access_token": access_token}