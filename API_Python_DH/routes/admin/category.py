from fastapi import APIRouter, HTTPException, status,Query
from controllers.admin import CategoryController
import models
from pydantic import BaseModel

router=APIRouter()

class CategoryBase(BaseModel):
    name: str

@router.get("/api/v1/admin/categories",status_code=status.HTTP_200_OK)
def indexCategory(page: int = Query(1, ge=1)):
    try:
        db_categories  = CategoryController.getCategory(page)
        return db_categories
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.post("/api/v1/admin/categories/store",status_code=status.HTTP_201_CREATED)
def storeCategory(category: CategoryBase):
    try:
        data_category = models.Category(**category.dict())
        db_category  = CategoryController.handleStoreCategory(data_category)
        print(db_category)
        return db_category
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.put("/api/v1/admin/categories/update/{category_id}",status_code=status.HTTP_201_CREATED)
def storeCategory(category_id:int,category:CategoryBase):
    try:
        data_category = models.Category(**category.dict())
        db_category = CategoryController.handleUpdateCategory(category_id,data_category)
        print(db_category)
        return db_category
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.delete("/api/v1/admin/categories/delete/{category_id}",status_code=status.HTTP_201_CREATED)
def deleteCategory(category_id:int):
    try:
        db_category  = CategoryController.handleDeleteCategory(category_id)
        print(db_category)
        return db_category
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.get("/api/v1/admin/categories/{category_id}",status_code=status.HTTP_201_CREATED)
def detailCategory(category_id:int):
    try:
        db_category  = CategoryController.handleDetailCategory(category_id)
        print(db_category)
        return db_category
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )