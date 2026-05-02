from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..controllers import reviews as controller
from ..schemas.reviews import ReviewCreate, ReviewUpdate, Review
from ..dependencies.database import get_db

router = APIRouter(prefix="/reviews", tags=["Reviews"])

@router.post("/", response_model=Review)
def create(request: ReviewCreate, db: Session = Depends(get_db)):
    return controller.create(db, request)

@router.get("/")
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{review_id}", response_model=Review)
def read_one(review_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, review_id)

@router.put("/{review_id}", response_model=Review)
def update(review_id: int, request: ReviewUpdate, db: Session = Depends(get_db)):
    return controller.update(db, review_id, request)

@router.delete("/{review_id}")
def delete(review_id: int, db: Session = Depends(get_db)):
    return controller.delete(db, review_id)
