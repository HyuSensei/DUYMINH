from fastapi import APIRouter, HTTPException, status
from controllers.user import OrderController
import models
from pydantic import BaseModel

router=APIRouter()

class CartBase(BaseModel):
    id: int
    price: float
    quantity: int
    class Config:
        arbitrary_types_allowed = True
    
class UserBase(BaseModel):
    name: str
    address: str
    phone: str
    user_id: int
    class Config:
        arbitrary_types_allowed = True

class OrderBase(BaseModel):
    cart: list[CartBase]
    user: UserBase
    class Config:
        arbitrary_types_allowed = True

@router.post("/api/v1/order",status_code=status.HTTP_201_CREATED)
def order(order: OrderBase):
    try:
        data_order = order.dict()
        get_data = OrderController.handleOrder(data_order)
        print(get_data)
        return get_data
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.get("/api/v1/orderWait/{id}",status_code=status.HTTP_200_OK)
def getOrderWait(id:int):
    try:
        get_data = OrderController.handleGetOrderWait(id)
        print(get_data)
        return get_data
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.get("/api/v1/orderShip/{id}",status_code=status.HTTP_200_OK)
def getOrderShip(id:int):
    try:
        get_data = OrderController.handleGetOrderShip(id)
        print(get_data)
        return get_data
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )


@router.get("/api/v1/orderComplete/{id}",status_code=status.HTTP_200_OK)
def getOrderComplete(id:int):
    try:
        get_data = OrderController.handleGetOrderComplete(id)
        print(get_data)
        return get_data
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.get("/api/v1/orderCancel/{id}",status_code=status.HTTP_200_OK)
def getOrderCancel(id:int):
    try:
        get_data = OrderController.handleGetOrderCancel(id)
        print(get_data)
        return get_data
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.get("/api/v1/actionCancelOrder/{id}",status_code=status.HTTP_200_OK)
def cancelOrder(id:int):
    try:
        get_data = OrderController.handlecancelOrder(id)
        print(get_data)
        return get_data
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.get("/api/v1/actionConfirmOrder/{id}",status_code=status.HTTP_200_OK)
def cancelOrder(id:int):
    try:
        get_data = OrderController.handleConfirmOrder(id)
        print(get_data)
        return get_data
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )