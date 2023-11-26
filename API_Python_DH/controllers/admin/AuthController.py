from fastapi import HTTPException, status
from database import SessionLocal
import models
import bcrypt
import jwt
from datetime import datetime, timedelta
def loginAdmin(user):
    db= SessionLocal()
    if (not user.username) or (not user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,detail="Vui lòng điền đầy đủ thông tin đăng nhập"
        )
    get_user = db.query(models.User).filter(models.User.username==user.username).first()
    if not get_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,detail="Tên đăng nhập không tồn tại vui lòng thử lại !"
        )
    check_password= checkPassword(user.password,get_user.password)
    if check_password==False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Mật khẩu không chính xác vui lòng thử lại !"
        )
    if get_user.role_id != 2:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Bạn không có quyền admin!"
        )
    else:
        token = createJWT(get_user.id)
        return {
        "success": True,
        "message": "Đăng nhập thành công !",
        "token": token,
        "user": get_user
    }
def checkPassword(password,hash_password):
    return bcrypt.checkpw(password.encode('utf-8'), hash_password.encode('utf-8'))    
def createJWT(user_id):
    now= datetime.utcnow()
    expire =now + timedelta(minutes=30)
    payload = {
        'user_id': user_id,
        'exp': expire,
        'iat': now
    }
    token = jwt.encode(payload, 'auth-key', algorithm='HS256')
    return token