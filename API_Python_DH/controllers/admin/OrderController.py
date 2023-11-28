from fastapi import HTTPException, status
from database import SessionLocal
from models import Order
import models 

def handleGetOrder(page):
    db=SessionLocal()
    get_order= db.query(models.Order)
    limit = 8
    start = (page - 1) * limit
    total = get_order.count()
    orders = get_order.offset(start).limit(limit).all()
    total_page = (total // limit) + (1 if total % limit > 0 else 0)
    current_page = page if page <= total_page else total_page
    return {
        "success":True,
        "orders":orders,
        "total_page":total_page,
        "current_page":current_page
    }

def handleDeleteOrder(order_id):
    db= SessionLocal()
    order = db.query(Order).filter(Order.id == order_id).first()
    if order is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail= "Đơn hàng không tồn tại !"
        )
    db.delete(order)
    db.commit()
    return {
        "success": True,
        "message":"Xóa thông tin đơn hàng thành công !",
    }

def handleConfirm(order_id):
    db=SessionLocal()
    order= db.query(models.Order).filter(models.Order.id==order_id).first()
    print(order)
    if order==None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Không tồn tại đơn hàng !"
        )
    else:
        order.status=1
        db.commit()
        return {
            "success":True,
            "message":"Duyệt đơn hàng thành công !"
        }