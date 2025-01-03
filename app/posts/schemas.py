from pydantic import BaseModel

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int

    class Config:
        from_attributes = True  # Allows Pydantic to parse ORM models
