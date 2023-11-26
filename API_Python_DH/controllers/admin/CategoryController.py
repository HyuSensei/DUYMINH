from fastapi import HTTPException, status
from database import SessionLocal
from models import Category 
def addCategories(categories):
    db= SessionLocal()
    if not categories.name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập tên danh mục sản phẩm !"
        )
    if db.query(Category).filter(Category.name == categories.name).all():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Tên danh mục đã tồn tại vui lòng nhập tên khác!"
        )
    db.add(categories)
    db.commit()
    db.refresh(categories)
    return {
        "success": True,
        "message":"Tạo danh mục thành công !",
        "categories": categories
    }
def getCategories():
    db= SessionLocal()
    categories = db.query(Category).all()
    if not categories:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Không tìm thấy danh mục sản phẩm !"
        )
    return {
        "success": True,
        "message":"Tìm danh mục thành công !",
        "categories": categories
    }