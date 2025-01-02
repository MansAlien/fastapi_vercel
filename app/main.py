from fastapi import FastAPI
from app.core.database import engine
from app.users.models import Base
from app.users.routes import router as user_router

# Create tables
Base.metadata.create_all(bind=engine)

# FastAPI app
app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["Users"])

