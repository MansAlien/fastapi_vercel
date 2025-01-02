from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.items.schemas import ItemCreate, ItemOut
from app.items.crud import get_items, create_item

router = APIRouter()

@router.get("/", response_model=list[ItemOut])
def read_items(db: Session = Depends(get_db)):
    return get_items(db)

@router.post("/", response_model=ItemOut)
def create_new_item(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db, item, owner_id=1)  # Default owner_id for simplicity

