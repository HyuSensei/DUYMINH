from fastapi import HTTPException, status
from database import SessionLocal
import models

def getBrand(page):
    db=SessionLocal()
    get_brand= db.query(models.Brand)
    limit = 8
    start = (page - 1) * limit
    total = get_brand.count()
    brands = get_brand.offset(start).limit(limit).all()
    total_page = (total // limit) + (1 if total % limit > 0 else 0)
    current_page = page if page <= total_page else total_page
    return {
        "success":True,
        "brand":brands,
        "total_page":total_page,
        "current_page":current_page
    }

def handleStoreBrand(Brand):
    db= SessionLocal()
    if not Brand.name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập đầy đủ thông tin thương hiệu !"
        )
    db.add(Brand)
    db.commit()
    db.refresh(Brand)
    return {
        "success": True,
        "message":"Thêm thương hiệu sản phẩm thành công !",
        "Brand": Brand
    }

def handleUpdateBrand(Brand_id,data_Brand):
    db= SessionLocal()
    if not data_Brand.name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập đầy đủ thông tin thương hiệu sản phẩm !"
        )
    Brand = db.query(models.Brand).filter(models.Brand.id == Brand_id).first()
    Brand.name = data_Brand.name
    db.commit()
    db.refresh(Brand)
    return {
        "success": True,
        "message":"Sửa thương hiệu sản phẩm thành công !",
        "Brand": Brand
    }

def handleDeleteBrand(Brand_id):
        db= SessionLocal()
        Brand = db.query(models.Brand).filter(models.Brand.id == Brand_id).first()
        if Brand is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail= "Thương hiệu sản phẩm không tồn tại !"
            )
        db.delete(Brand)
        db.commit()
        return {
            "success": True,
            "message":"Xóa thương hiệu sản phẩm thành công !",
        }

def handleDetailBrand(Brand_id):
        db= SessionLocal()
        Brand = db.query(models.Brand).filter(models.Brand.id == Brand_id).first()
        if Brand is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail= "Thương hiệu sản phẩm không tồn tại !"
            )
        return {
            "success": True,
            "brand":Brand
        }