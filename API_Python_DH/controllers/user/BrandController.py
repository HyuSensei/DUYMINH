from fastapi import HTTPException, status
from database import SessionLocal
import models

def handleGetBrand():
    db=SessionLocal()
    brands= db.query(models.Brand).all()
    return {
        "success":True,
        "brands":brands
    }

def handleBrand(id,page):
    db=SessionLocal()
    get_brand= db.query(models.Brand).all()
    limit = 8
    start = (page - 1) * limit
    get_product= db.query(models.Product).filter(models.Product.brand_id==id)
    total = get_product.count()
    products = get_product.offset(start).limit(limit).all()
    total_page = (total // limit) + (1 if total % limit > 0 else 0)
    current_page = page if page <= total_page else total_page
    return {
        "success":True,
        "brand_id":id,
        "brands":get_brand,
        "products":products,
        "total_page":total_page,
        "current_page":current_page
    }