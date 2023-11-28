from fastapi import APIRouter, HTTPException, status,Query
from controllers.admin import BrandController
import models
from pydantic import BaseModel

router=APIRouter()

class BrandBase(BaseModel):
    name: str

@router.get("/api/v1/admin/brands",status_code=status.HTTP_200_OK)
def indexBrand(page: int = Query(1, ge=1)):
    try:
        db_brands  = BrandController.getBrand(page)
        return db_brands
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.post("/api/v1/admin/brands/store",status_code=status.HTTP_201_CREATED)
def storeBrand(Brand: BrandBase):
    try:
        data_Brand = models.Brand(**Brand.dict())
        db_Brand  = BrandController.handleStoreBrand(data_Brand)
        print(db_Brand)
        return db_Brand
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.put("/api/v1/admin/brands/update/{brand_id}",status_code=status.HTTP_201_CREATED)
def storeBrand(brand_id:int,Brand:BrandBase):
    try:
        data_Brand = models.Brand(**Brand.dict())
        db_Brand = BrandController.handleUpdateBrand(brand_id,data_Brand)
        print(db_Brand)
        return db_Brand
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.delete("/api/v1/admin/brands/delete/{brand_id}",status_code=status.HTTP_201_CREATED)
def deleteBrand(brand_id:int):
    try:
        db_Brand  = BrandController.handleDeleteBrand(brand_id)
        print(db_Brand)
        return db_Brand
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )


@router.get("/api/v1/admin/brands/{brand_id}",status_code=status.HTTP_201_CREATED)
def detailBrand(brand_id:int):
    try:
        db_Brand  = BrandController.handleDetailBrand(brand_id)
        print(db_Brand)
        return db_Brand
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )