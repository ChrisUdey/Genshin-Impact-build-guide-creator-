from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    # JWT
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_HOURS: int = 24

    # File Upload
    UPLOAD_DIR: str = "uploads"
    MAX_FILE_SIZE: int = 2 * 1024 * 1024  # 2MB
    ALLOWED_EXTENSIONS: list = ["jpg", "jpeg", "png", "webp"]

    # Database - FIXED PATH
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATABASE_URL: str = f"sqlite:///{BASE_DIR}/genshin_builds.db"

    # CORS
    FRONTEND_URL: str = "http://localhost:3000"

    class Config:
        env_file = ".env"


settings = Settings()