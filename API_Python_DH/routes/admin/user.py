from fastapi import APIRouter, HTTPException, status, Path
from controllers.admin import UserController
import models
from database import SessionLocal
from pydantic import BaseModel

router=APIRouter()

class UserBase(BaseModel):
    name : str
    email : str
    username : str
    password : str
    address : str
    role_id : int
@router.get("/api/v1/countUser",status_code=status.HTTP_200_OK)
async def countUser():
    try:
        db_User  = UserController.countUser()
        return db_User
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        ) 
@router.get("/api/v1/user/limit/{currentPage}",status_code=status.HTTP_200_OK)
async def getUser(currentPage : int = Path(..., title="page", ge=1)):
    try:
        db_User  = UserController.getUsers(currentPage)
        return db_User
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.post("/addUser/",status_code=status.HTTP_201_CREATED)
async def addUser(user: UserBase):
    try:
        data_user = models.User(**user.dict())
        db_user  = UserController.addUser(data_user)
        return db_user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.get("/api/v1/user/{user_id}",status_code=status.HTTP_200_OK)
async def getUsersById(user_id: int = Path(..., title="id người dùng", ge=1)):
    try:
        db_user  = UserController.getUserById(user_id)
        return db_user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.get("/api/v1/userByUserName/{username}",status_code=status.HTTP_200_OK)
async def getUsersByUserName(username: str = Path(..., title="nhap ten nguoi dung")):
    try:
        db_user  = UserController.getUserByUserName(username)
        return db_user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.get("/api/v1/userByUserNamePage/{username}/page/{currentPage}",status_code=status.HTTP_200_OK)
async def getUsersByUserNamePage(username: str, currentPage: int = Path(..., title="nhap ten nguoi dung")):
    try:
        db_user  = UserController.getUsersByUserNamePage(username, currentPage)
        return db_user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.put("/api/v1/updateUser/{user_id}",status_code=status.HTTP_201_CREATED)
async def updateUsers(user_id: int , user_data: UserBase):
    try:
        data_user = models.User(**user_data.dict())
        db_user   = UserController.updateUser(user_id, data_user)
        return db_user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.delete("/api/v1/deleteUser/{user_id}",status_code=status.HTTP_201_CREATED)
async def deleteUsers(user_id: int):
    try:
        db_user  = UserController.deleteUser(user_id)
        return db_user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )