from pydantic import BaseModel

class ItemBase(BaseModel):
    title: str
    description: str

class ItemCreate(ItemBase):
    pass

class ItemOut(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

