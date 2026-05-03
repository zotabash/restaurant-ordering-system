from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import orders as model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = model.Order(
        customer_id=request.customer_id,
        order_date=request.order_date,
        tracking_number=request.tracking_number,
        status=request.status,
        total_price=request.total_price,
        promo_id=request.promo_id
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error
        )

    return new_item


def read_all(db: Session):
    return db.query(model.Order).all()


def read_one(db: Session, item_id):
    item = db.query(model.Order).filter(
        model.Order.id == item_id
    ).first()

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Id not found!"
        )

    return item


def update(db: Session, item_id, request):
    item = db.query(model.Order).filter(
        model.Order.order_id == item_id
    )

    if not item.first():
        raise HTTPException(
            status_code=404,
            detail="Id not found!"
        )

    update_data = request.dict(exclude_unset=True)
    item.update(update_data)

    db.commit()

    return item.first()


def delete(db: Session, item_id):

    item = db.query(model.Order).filter(
        model.Order.order_id == item_id   # ✅ MUST be order_id
    ).first()

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Id not found!"
        )

    db.delete(item)
    db.commit()

    return {"message": "Deleted successfully"}