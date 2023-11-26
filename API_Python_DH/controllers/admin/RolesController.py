from fastapi import HTTPException, status
from database import SessionLocal
from models import Role 
def addRole(role):
    db= SessionLocal()
    if not role.name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập tên role!"
        )
    role_check = db.query(Role).filter(Role.name == role.name).first()
    if role_check:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Tên role đã tồn tại!"
        )
    db.add(role)
    db.commit()
    db.refresh(role)
    return {
        "success": True,
        "message":"Tạo role thành công !",
        "role": role
    }
def getRoles():
    db= SessionLocal()
    role = db.query(Role).all()
    if not role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Không tìm thấy role !"
        )
    return {
        "success": True,
        "message":"Tìm role thành công !",
        "role": role
    }