from fastapi import APIRouter, HTTPException, status
from controllers.admin import CategoryController
import models
from database import SessionLocal
from pydantic import BaseModel

router=APIRouter()

class CategoriesBase(BaseModel):
    name: str

@router.post("/addCategories/",status_code=status.HTTP_201_CREATED)
async def addCategories(categories: CategoriesBase):
    try:
        data_categories = models.Category(**categories.dict())
        db_categories  = CategoryController.addCategories(data_categories)
        return db_categories
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
@router.get("/api/v1/getAllCategories/",status_code=status.HTTP_200_OK)
async def getAllCategories():
    try:
        db_categories  = CategoryController.getCategories()
        return db_categories
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )