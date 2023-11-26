from fastapi import HTTPException, status
from database import SessionLocal
import models

def handleProductHome():
    db=SessionLocal()
    get_product= db.query(models.Product).filter(models.Product.category_id==1).all()
    return {
        "success":True,
        "product":get_product
    }
    
def storeProduct(product):
    db=SessionLocal()
    db.add(product)
    db.commit()
    db.refresh(product)
    return {
        "success": True,
        "message": "Thêm sản phẩm thành công !",
        "product": product
    }

def handleProductDetail(product_id):
    db=SessionLocal()
    product= db.query(models.Product).filter(models.Product.id==product_id).first()
    return {
        "id": product.id,
        "name":product.name,
        "image":product.image,
        "price":product.price,
        "description":product.description,
        "brand_id":product.brand_id,
        "category_id":product.category_id
    }
    
def handleSearchProduct(product_name,page):
    db=SessionLocal()
    limit = 8
    start = (page - 1) * limit
    query = db.query(models.Product)
    if product_name:
        query = query.filter(models.Product.name.ilike(f"%{product_name}%"))
    total = query.count()
    products = query.offset(start).limit(limit).all()
    total_page = (total // limit) + (1 if total % limit > 0 else 0)
    current_page = page if page <= total_page else total_page
    return {
        "success": True,
        "total": total,
        "total_page":total_page,
        "current_page": current_page,
        "products": products
    }

 

    
    