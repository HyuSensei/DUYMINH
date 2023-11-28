from fastapi import APIRouter, HTTPException, status,Path,Query
from controllers.admin import ProductController
import models
from database import SessionLocal
from pydantic import BaseModel

router=APIRouter()

class ProductsBase(BaseModel):
    name: str
    image: str
    price: str
    description: str
    brand_id: str
    category_id: str

@router.get("/api/v1/admin/products",status_code=status.HTTP_200_OK)
def indexProduct(page: int = Query(1, ge=1)):
    try:
        db_product  = ProductController.getProduct(page)
        return db_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.post("/api/v1/admin/products/store",status_code=status.HTTP_201_CREATED)
def storeProduct(product: ProductsBase):
    try:
        data_product = models.Product(**product.dict())
        db_product  = ProductController.handleStoreProduct(data_product)
        print(db_product)
        return db_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.put("/api/v1/admin/products/update/{product_id}",status_code=status.HTTP_201_CREATED)
def storeProduct(product_id:int,product:ProductsBase):
    try:
        data_product = models.Product(**product.dict())
        db_product  = ProductController.handleUpdateProduct(data_product,product_id)
        print(db_product)
        return db_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.delete("/api/v1/admin/products/delete/{product_id}",status_code=status.HTTP_201_CREATED)
def deleteProduct(product_id):
    try:
        db_product  = ProductController.handleDeleteProduct(product_id)
        print(db_product)
        return db_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )