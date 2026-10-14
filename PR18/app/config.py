from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "sqlite:///./cloud_app.db"
    storage_path: str = "storage/objects"
    max_upload_size: int = 5 * 1024 * 1024  # 5 МБ

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()