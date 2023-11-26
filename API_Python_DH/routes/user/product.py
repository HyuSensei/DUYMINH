from fastapi import APIRouter, HTTPException, status, Query
from controllers.user import ProductController
from pydantic import BaseModel
import models

router=APIRouter()

@router.get("/api/v1/products/home",status_code=status.HTTP_200_OK)
def getProductHome():
    try:
        data= ProductController.handleProductHome()
        print(data)
        return data
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.get("/api/v1/products/{product_id}",status_code=status.HTTP_200_OK)
def getProductDetail(product_id: int):
    try:
        get_product= ProductController.handleProductDetail(product_id)
        return get_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.get("/api/v1/products/search/{product_name}",status_code=status.HTTP_200_OK)
def getProductSearch(
    product_name: str,
    page: int = Query(1, ge=1),
):
    try:
        get_product= ProductController.handleSearchProduct(product_name,page)
        return get_product
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )
