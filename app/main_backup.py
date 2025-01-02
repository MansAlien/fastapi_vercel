from fastapi import FastAPI
from app.users.routes import router as users_router
from app.items.routes import router as items_router

from app.core.database import engine, SessionLocal
from app.users.models import Base, User

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(title="Folder-by-Feature FastAPI Project")

# Include feature routers
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(items_router, prefix="/items", tags=["Items"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI project!"}

