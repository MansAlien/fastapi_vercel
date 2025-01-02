from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./data/test.db"
    SECRET_KEY: str = "your-secret-key"
    DEBUG: bool = True

settings = Settings()

