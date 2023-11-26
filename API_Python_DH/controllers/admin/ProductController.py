from fastapi import HTTPException, status
from database import SessionLocal
from models import Product 
from sqlalchemy import func

def addProduct(product):
    try:
        db= SessionLocal()
        if not product.name:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập tên sản phẩm !"
            )
        if not product.image:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập ảnh sản phẩm !"
            )
        if not product.price:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập giá sản phẩm !"
            )
        if not product.category_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập sanh mục sản phẩm !"
            )
        db.add(product)
        db.commit()
        db.refresh(product)
        return {
            "success": True,
            "message":"Thêm sản phẩm thành công!",
            "product": product
        }
    except Exception as e:
        return {
            "success": False,
            "message":"Thêm sản phẩm thất bại!",
            "err": e
        }
def getProducts(currentPage):
    try:
        limit = 6
        offset = (currentPage - 1) * limit
        db = SessionLocal()
        products = db.query(Product).limit(limit).offset(offset).all()
        return {
            "success": True,
            "message": "Tìm sản phẩm thành công!",
            "products": products
        }
    except Exception as e:
        return {
            "success": False,
            "message": "Tìm sản phẩm thất bại!",
            "err": str(e)
        }
def countProducts():
    try:
        db = SessionLocal()
        product_count = db.query(func.count(Product.id)).scalar()
        return {
            "success": True,
            "message": "Số lượng sản phẩm đã được đếm!",
            "data": product_count
        }
    except Exception as e:
        return {
            "success": False,
            "message": "Đếm sản phẩm thất bại!",
            "err": str(e)
        }
def getProductById(product_id):
    try:
        db= SessionLocal()
        product = db.query(Product).filter(Product.id == product_id).first()
        return {
            "success": True,
            "message":"Tìm sản phẩm thành công!",
            "product": product
        }
    except Exception as e:
        return {
            "success": False,
            "message":"Tìm sản phẩm thất bại!",
            "err": e
        }
def getProductByNamePage(product_name, currentPage):
    try:
        limit = 6
        offset = (currentPage - 1) * limit
        db= SessionLocal()
        product = db.query(Product).filter(Product.name.like(f"%{product_name}%")).limit(limit).offset(offset).all()
        return {
            "success": True,
            "message":"Tìm sản phẩm thành công!",
            "product": product
        }
    except Exception as e:
        return {
            "success": False,
            "message":"Tìm sản phẩm thất bại!",
            "err": e
        }
def getProductByName(product_name):
    try:
        db= SessionLocal()
        product = db.query(Product).filter(Product.name.like(f"%{product_name}%")).all()
        return {
            "success": True,
            "message":"Tìm sản phẩm thành công!",
            "product": product
        }
    except Exception as e:
        return {
            "success": False,
            "message":"Tìm sản phẩm thất bại!",
            "err": e
        }
def updateProduct(product_id, product_data):
    try:
        db= SessionLocal()
        product = db.query(Product).filter(Product.id == product_id).first()

        if product is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Sản phẩm không tòn tại !"
            )
        if not product_data.name:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập tên sản phẩm !"
            )
        # if not product_data.image:
        #     raise HTTPException(
        #         status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập ảnh sản phẩm !"
        #     )
        if not product_data.price:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập giá sản phẩm !"
            )
        if not product_data.category_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập sanh mục sản phẩm !"
            )
        product.name = product_data.name
        if product_data.image:
            product.image = product_data.image
        product.price = product_data.price
        product.category_id = product_data.category_id
        db.commit()
        db.refresh(product)
        return {
            "success": True,
            "message":"Sửa sản phẩm thành công!",
            "product": product
        }
    except Exception as e:
        return {
            "success": False,
            "message":"Sửa sản phẩm thất bại!",
            "err": e
        }
        
def deleteProduct(product_id):
    try:
        db= SessionLocal()
        product = db.query(Product).filter(Product.id == product_id).first()

        if product is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Sản phẩm không tòn tại !"
            )
        db.delete(product)
        db.commit()
        return {
            "success": True,
            "message":"Xóa sản phẩm thành công!",
        }
    except Exception as e:
        return {
            "success": False,
            "message":"Xóa sản phẩm thất bại!",
            "err": e
        }