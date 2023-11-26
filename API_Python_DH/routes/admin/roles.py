from fastapi import APIRouter, HTTPException, status
from controllers.admin import RolesController
import models
from database import SessionLocal
from pydantic import BaseModel

router=APIRouter()

class RolesBase(BaseModel):
    name: str

@router.post("/addRole/",status_code=status.HTTP_201_CREATED)
async def addRole(role: RolesBase):
    try:
        data_role = models.Role(**role.dict())
        db_role  = RolesController.addRole(data_role)
        return db_role
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.get("/api/v1/getAllRole/",status_code=status.HTTP_200_OK)
async def getRole():
    try:
        db_role  = RolesController.getRoles()
        return db_role
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )