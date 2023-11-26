from fastapi import APIRouter, HTTPException, status, Path
from controllers.admin import AuthController
import models
from database import SessionLocal
from pydantic import BaseModel

router=APIRouter()

class UserRegisterBase(BaseModel):
    name: str
    email: str
    username: str
    password: str
    address: str
    role_id: int
    class Config:
        arbitrary_types_allowed = True

class UserLogin(BaseModel):
    username: str
    password: str
    class Config:
        arbitrary_types_allowed = True
@router.post("/api/v1/loginAdmin/",status_code=status.HTTP_201_CREATED)
async def loginAdmin(user: UserLogin):
    try:
        data_user = models.User(**user.dict())
        db_user  = AuthController.loginAdmin(data_user)
        return db_user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )