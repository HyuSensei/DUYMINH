from fastapi import APIRouter, HTTPException, status,Query
from controllers.admin import OrderController

router=APIRouter()

@router.get("/api/v1/admin/orders",status_code=status.HTTP_200_OK)
def indexOrder(page: int = Query(1, ge=1)):
    try:
        db_order  = OrderController.handleGetOrder(page)
        return db_order
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.delete("/api/v1/admin/orders/delete/{order_id}",status_code=status.HTTP_200_OK)
def deleteOrder(order_id:int):
    try:
        db_order  = OrderController.handleDeleteOrder(order_id)
        return db_order
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )

@router.get("/api/v1/admin/orders/confirm/{order_id}",status_code=status.HTTP_200_OK)
def confirmOrder(order_id:int):
    try:
        db_order  = OrderController.handleConfirm(order_id)
        return db_order
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )