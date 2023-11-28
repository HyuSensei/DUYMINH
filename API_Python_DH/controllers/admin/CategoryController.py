from fastapi import HTTPException, status
from database import SessionLocal
from models import Category 
import models

def getCategory(page):
    db=SessionLocal()
    get_category= db.query(models.Category)
    limit = 8
    start = (page - 1) * limit
    total = get_category.count()
    categories = get_category.offset(start).limit(limit).all()
    total_page = (total // limit) + (1 if total % limit > 0 else 0)
    current_page = page if page <= total_page else total_page
    return {
        "success":True,
        "categories":categories,
        "total_page":total_page,
        "current_page":current_page
    }
    
def handleStoreCategory(category):
    db= SessionLocal()
    if not category.name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập đầy đủ thông tin danh mục !"
        )
    db.add(category)
    db.commit()
    db.refresh(category)
    return {
        "success": True,
        "message":"Thêm danh mục sản phẩm thành công !",
        "category": category
    }

def handleUpdateCategory(category_id,data_category):
    db= SessionLocal()
    if not data_category.name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập đầy đủ thông tin danh mục sản phẩm !"
        )
    category = db.query(Category).filter(Category.id == category_id).first()
    category.name = data_category.name
    db.commit()
    db.refresh(category)
    return {
        "success": True,
        "message":"Sửa danh mục sản phẩm thành công !",
        "category": category
    }

def handleDeleteCategory(category_id):
        db= SessionLocal()
        category = db.query(Category).filter(Category.id == category_id).first()
        if category is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail= "Danh mục sản phẩm không tòn tại !"
            )
        db.delete(category)
        db.commit()
        return {
            "success": True,
            "message":"Xóa danh mục sản phẩm thành công !",
        }
        
def handleDetailCategory(category_id):
        db= SessionLocal()
        category = db.query(Category).filter(Category.id == category_id).first()
        if category is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail= "Danh mục sản phẩm không tòn tại !"
            )
        return {
            "success": True,
            "category":category
        }