from fastapi import HTTPException, status
from database import SessionLocal
import models

def handleGetCategory():
    db=SessionLocal()
    categories= db.query(models.Category).all()
    return {
        "success":True,
        "categories":categories
    }

def handleProductCategory(id,page):
    db=SessionLocal()
    get_category= db.query(models.Category).all()
    limit = 8
    start = (page - 1) * limit
    get_product= db.query(models.Product).filter(models.Product.category_id==id)
    total = get_product.count()
    products = get_product.offset(start).limit(limit).all()
    total_page = (total // limit) + (1 if total % limit > 0 else 0)
    current_page = page if page <= total_page else total_page
    return {
        "success":True,
        "category_id":id,
        "categories":get_category,
        "products":products,
        "total_page":total_page,
        "current_page":current_page
    }