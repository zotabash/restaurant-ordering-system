from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response
from ..models import order_details as model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = model.OrderDetail(
        order_id=request.order_id,
        sandwich_id=request.sandwich_id,
        amount=request.amount
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
    return db.query(model.OrderDetail).all()


def read_one(db: Session, item_id):
    item = db.query(model.OrderDetail).filter(
        model.OrderDetail.id == item_id
    ).first()

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Id not found!"
        )

    return item


def update(db: Session, item_id, request):
    item = db.query(model.OrderDetail).filter(
        model.OrderDetail.id == item_id
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
    item = db.query(model.OrderDetail).filter(
        model.OrderDetail.id == item_id
    )

    if not item.first():
        raise HTTPException(
            status_code=404,
            detail="Id not found!"
        )

    item.delete()
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
