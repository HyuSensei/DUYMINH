from fastapi import HTTPException, status
from database import SessionLocal
from models import User
from sqlalchemy import func

def getUsers(currentPage):
    try:
        limit = 6
        offset = (currentPage - 1) * limit
        db = SessionLocal()
        user = db.query(User).limit(limit).offset(offset).all()
        return {
            "success": True,
            "message": "Tìm người dùng thành công!",
            "users": user
        }
    except Exception as e:
        return {
            "success": False,
            "message": "Tìm người dùng thất bại!",
            "err": str(e)
        }
def countUser():
    try:
        db = SessionLocal()
        user_count = db.query(func.count(User.id)).scalar()
        return {
            "success": True,
            "message": "Số lượng người dùng đã được đếm!",
            "data": user_count
        }
    except Exception as e:
        return {
            "success": False,
            "message": "Đếm người dùng thất bại!",
            "err": str(e)
        }
def addUser(user):
    try:
        db = SessionLocal()
        if not user.name:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập tên người dùng !"
            )
        
        if not user.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập email người dùng !"
            )
        user_check1 = db.query(User).filter(User.email == user.email).first()
        if user_check1:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Email đã tồn tại người dùng !"
            )
        if not user.username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập username người dùng !"
            )
        user_check = db.query(User).filter(User.username == user.username).first()
        if user_check:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Tên người dùng đã tồn tại người dùng !"
            )
        if not user.password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập password người dùng !"
            )
        if not user.address:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập địa chỉ người dùng !"
            )
        if not user.role_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập role người dùng !"
            )
        db.add(user)
        db.commit()
        db.refresh(user)
        return {
            "success": True,
            "message":"Thêm người dùng thành công!",
            "user": user
        }
    except Exception as e:
        return {
            "success": False,
            "message":"Thêm người dùng thất bại!",
            "err": e
        }
def getUserById(user_id):
    try:
        db= SessionLocal()
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Người dùng không tồn tại!"
            )
        return {
            "success": True,
            "message":"Tìm người dùng thành công!",
            "user": user
        }
    except Exception as e:
        return {
            "success": False,
            "message":"Tìm người dùng thất bại!",
            "err": e
        }
def getUserByUserName(username):
    try:
        db= SessionLocal()
        user = db.query(User).filter(User.username.like(f"%{username}%")).all()
        if len(user) <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Người dùng không tồn tại!"
            )
        return {
            "success": True,
            "message":"Tìm người dùng thành công!",
            "user": user
        }
    except Exception as e:
        return {
            "success": False,
            "message":"Tìm người dùng thất bại!",
            "err": e
        }
def getUsersByUserNamePage(username, currentPage):
    try:
        limit = 6
        offset = (currentPage - 1) * limit
        db= SessionLocal()
        user = db.query(User).filter(User.username.like(f"%{username}%")).limit(limit).offset(offset).all()
        return {
            "success": True,
            "message":"Tìm người dùng thành công!",
            "user": user
        }
    except Exception as e:
        return {
            "success": False,
            "message":"Tìm người dùng thất bại!",
            "err": e
        }
def updateUser(user_id, user_data):
    try:
        db= SessionLocal()
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Người dùng không tòn tại !"
            )
        if not user.name:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập tên người dùng !"
            )
        
        if not user.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập email người dùng !"
            )
        if not user.username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập username người dùng !"
            )
        if not user.password:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập password người dùng !"
            )
        if not user.address:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập địa chỉ người dùng !"
            )
        if not user.role_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Vui lòng nhập role người dùng !"
            )
        user.name = user_data.name
        user.email = user_data.email
        user.username = user_data.username
        user.password = user_data.password
        user.address = user_data.address
        user.role_id = user_data.role_id
        db.commit()
        db.refresh(user)
        return {
            "success": True,
            "message":"Sửa người dùng thành công!",
            "user": user
        }
    except Exception as e:
        return {
            "success": False,
            "message":"Sửa người dùng thất bại!",
            "err": e
        }
        
def deleteUser(user_id):
    try:
        db= SessionLocal()
        user = db.query(User).filter(User.id == user_id).first()

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Người dùng không tồn tại !"
            )
        db.delete(user)
        db.commit()
        return {
            "success": True,
            "message":"Xóa người dùng thành công!",
        }
    except Exception as e:
        return {
            "success": False,
            "message":"Xóa người dùng thất bại!",
            "err": e
        }