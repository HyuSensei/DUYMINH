from fastapi import HTTPException, status
from database import SessionLocal
import models 
from sqlalchemy import func

def handleOrder(data_order):
    db= SessionLocal()
    data_cart= data_order["cart"]
    if len(data_cart)==0:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST, detail="Vui lòng thêm sản phẩm vào giỏ hàng !"
        )
    data_user= data_order["user"]
    if (not data_user["name"]) or (not data_user["address"]) or (not data_user["phone"]) or (not data_user["user_id"]):
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST, detail="Vui lòng điền đầy đủ thông tin đặt hàng !"
        )
    total=0
    for i in range(len(data_cart)):
        total = data_cart[i]["price"] * data_cart[i]["quantity"]
    order_info = models.Order(
    status=0,
    name=data_user["name"],
    address=data_user["address"],
    phone=data_user["phone"],
    total=total,
    user_id=data_user["user_id"]
    )
    db.add(order_info)
    db.commit()
    max_id_order = db.query(func.max(models.Order.id)).scalar()
    for i in range(len(data_cart)):
       order_product= models.OrderProduct(
           order_id= max_id_order,
           product_id= data_cart[i]["id"],
           quantity= data_cart[i]["quantity"]
       )
       db.add(order_product)
       db.commit()
    return {
        "success": True,
        "message": "Đặt hàng thành công !",
    }


def handleGetOrderWait(id):
    db=SessionLocal()
    query = (
    db.query(models.Order, models.Product,models.OrderProduct)
    .join(models.OrderProduct, models.Order.id == models.OrderProduct.order_id)
    .join(models.Product, models.OrderProduct.product_id == models.Product.id)
    .filter(models.Order.user_id == id)
    .filter(models.Order.status == 0)
    )
    results = query.all()
    data_order=[]
    last_product=[]
    max_order=[]
    get_last_product=[]
    for order, product, order_product in results:
        get_order={
            "id":order.id,
            "status": order.status,
            "name": order.name,
            "address": order.address,
            "phone": order.phone,
            "user_id": order.user_id,
            "total": order.total,
            "product_id": order_product.product_id,
            "quantity": order_product.quantity,
            "product_price": product.price,
            "product_name": product.name,
            "product_image": product.image 
        }
        check_last_order = db.query(func.max(models.OrderProduct.id)).filter(models.OrderProduct.order_id == order.id).scalar()
        if check_last_order not in max_order:
            max_order.append(check_last_order)
        data_order.append(get_order)
    for i in max_order:
        check_last_product= db.query(models.OrderProduct.product_id).filter(models.OrderProduct.id == i).first()
        last_product.append(check_last_product)
    get_last_product = [result[0] for result in last_product]
    return {
        "success":True,
        "message":"Thông tin đơn hàng đang chờ xác nhận !",
        "order": data_order,
        "last_product": get_last_product
    }

def handleGetOrderShip(id):
    db=SessionLocal()
    query = (
    db.query(models.Order, models.Product,models.OrderProduct)
    .join(models.OrderProduct, models.Order.id == models.OrderProduct.order_id)
    .join(models.Product, models.OrderProduct.product_id == models.Product.id)
    .filter(models.Order.user_id == id)
    .filter(models.Order.status == 1)
    )
    results = query.all()
    data_order=[]
    last_product=[]
    max_order=[]
    get_last_product=[]
    for order, product, order_product in results:
        get_order={
            "id":order.id,
            "status": order.status,
            "name": order.name,
            "address": order.address,
            "phone": order.phone,
            "user_id": order.user_id,
            "total": order.total,
            "product_id": order_product.product_id,
            "quantity": order_product.quantity,
            "product_price": product.price,
            "product_name": product.name,
            "product_image": product.image 
        }
        check_last_order = db.query(func.max(models.OrderProduct.id)).filter(models.OrderProduct.order_id == order.id).scalar()
        if check_last_order not in max_order:
            max_order.append(check_last_order)
        data_order.append(get_order)
    for i in max_order:
        check_last_product= db.query(models.OrderProduct.product_id).filter(models.OrderProduct.id == i).first()
        last_product.append(check_last_product)
    get_last_product = [result[0] for result in last_product]
    return {
        "success":True,
        "message":"Thông tin đơn hàng đang vận chuyển !",
        "order": data_order,
        "last_product": get_last_product
    }

def handleGetOrderComplete(id):
    db=SessionLocal()
    query = (
    db.query(models.Order, models.Product,models.OrderProduct)
    .join(models.OrderProduct, models.Order.id == models.OrderProduct.order_id)
    .join(models.Product, models.OrderProduct.product_id == models.Product.id)
    .filter(models.Order.user_id == id)
    .filter(models.Order.status == 2)
    )
    results = query.all()
    data_order=[]
    last_product=[]
    max_order=[]
    get_last_product=[]
    for order, product, order_product in results:
        get_order={
            "id":order.id,
            "status": order.status,
            "name": order.name,
            "address": order.address,
            "phone": order.phone,
            "user_id": order.user_id,
            "total": order.total,
            "product_id": order_product.product_id,
            "quantity": order_product.quantity,
            "product_price": product.price,
            "product_name": product.name,
            "product_image": product.image 
        }
        check_last_order = db.query(func.max(models.OrderProduct.id)).filter(models.OrderProduct.order_id == order.id).scalar()
        if check_last_order not in max_order:
            max_order.append(check_last_order)
        data_order.append(get_order)
    for i in max_order:
        check_last_product= db.query(models.OrderProduct.product_id).filter(models.OrderProduct.id == i).first()
        last_product.append(check_last_product)
    get_last_product = [result[0] for result in last_product]
    return {
        "success":True,
        "message":"Thông tin đơn hàng đã hoàn thành!",
        "order": data_order,
        "last_product": get_last_product
    }


def handleGetOrderCancel(id):
    db=SessionLocal()
    query = (
    db.query(models.Order, models.Product,models.OrderProduct)
    .join(models.OrderProduct, models.Order.id == models.OrderProduct.order_id)
    .join(models.Product, models.OrderProduct.product_id == models.Product.id)
    .filter(models.Order.user_id == id)
    .filter(models.Order.status == 3)
    )
    results = query.all()
    data_order=[]
    last_product=[]
    max_order=[]
    get_last_product=[]
    for order, product, order_product in results:
        get_order={
            "id":order.id,
            "status": order.status,
            "name": order.name,
            "address": order.address,
            "phone": order.phone,
            "user_id": order.user_id,
            "total": order.total,
            "product_id": order_product.product_id,
            "quantity": order_product.quantity,
            "product_price": product.price,
            "product_name": product.name,
            "product_image": product.image 
        }
        check_last_order = db.query(func.max(models.OrderProduct.id)).filter(models.OrderProduct.order_id == order.id).scalar()
        if check_last_order not in max_order:
            max_order.append(check_last_order)
        data_order.append(get_order)
    for i in max_order:
        check_last_product= db.query(models.OrderProduct.product_id).filter(models.OrderProduct.id == i).first()
        last_product.append(check_last_product)
    get_last_product = [result[0] for result in last_product]
    return {
        "success":True,
        "message":"Thông tin đơn hàng đã hủy!",
        "order": data_order,
        "last_product": get_last_product
    }


def handlecancelOrder(id):
    db=SessionLocal()
    order= db.query(models.Order).filter(models.Order.id==id).first()
    print(order)
    if order==None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Không tồn tại đơn hàng !"
        )
    else:
        order.status=3
        db.commit()
        return {
            "success":True,
            "message":"Hủy đơn hàng thành công !"
        }

def handleConfirmOrder(id):
    db=SessionLocal()
    order= db.query(models.Order).filter(models.Order.id==id).first()
    print(order)
    if order==None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Không tồn tại đơn hàng !"
        )
    else:
        order.status=2
        db.commit()
        return {
            "success":True,
            "message":"Xác nhận đã nhận hàng thành công !"
        }