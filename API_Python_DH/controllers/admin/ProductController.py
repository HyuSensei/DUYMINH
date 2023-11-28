from fastapi import HTTPException, status
from database import SessionLocal
from models import Product 
import models

def getProduct(page):
    db=SessionLocal()
    get_product= db.query(models.Product)
    limit = 8
    start = (page - 1) * limit
    total = get_product.count()
    products = get_product.offset(start).limit(limit).all()
    total_page = (total // limit) + (1 if total % limit > 0 else 0)
    current_page = page if page <= total_page else total_page
    return {
        "success":True,
        "products":products,
        "total_page":total_page,
        "current_page":current_page
    }

def handleStoreProduct(product):
    print(product)
    db= SessionLocal()
    if not product.name or not product.image or not product.price or not product.description or not product.brand_id or not product.category_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập đầy đủ thông tin sản phẩm !"
        )
    db.add(product)
    product.image= "/images/products/"+product.image
    db.commit()
    db.refresh(product)
    return {
        "success": True,
        "message":"Thêm sản phẩm thành công !",
        "product": product
    }
    
def handleUpdateProduct(data_product,product_id):
    db= SessionLocal()
    if not data_product.name or not data_product.image or not data_product.price or not data_product.description or not data_product.brand_id or not data_product.category_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập đầy đủ thông tin sản phẩm !"
        )
    product = db.query(Product).filter(Product.id == product_id).first()
    product.name = data_product.name
    if product.image:
        product.image = data_product.image
    product.price = data_product.price
    product.description = data_product.description
    product.brand_id = data_product.brand_id
    product.category_id = data_product.category_id
    db.commit()
    db.refresh(product)
    return {
        "success": True,
        "message":"Sửa sản phẩm thành công !",
        "product": product
    }
    
def handleDeleteProduct(product_id):
        db= SessionLocal()
        product = db.query(Product).filter(Product.id == product_id).first()
        if product is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail= "Sản phẩm không tòn tại !"
            )
        db.delete(product)
        db.commit()
        return {
            "success": True,
            "message":"Xóa sản phẩm thành công !",
        }