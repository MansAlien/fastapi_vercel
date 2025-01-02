from sqlalchemy.orm import Session
from app.items.models import Item
from app.items.schemas import ItemCreate

def get_items(db: Session):
    return db.query(Item).all()

def create_item(db: Session, item: ItemCreate, owner_id: int):
    db_item = Item(**item.dict(), owner_id=owner_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

