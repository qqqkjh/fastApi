from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Test Fast API"
    admin_email: str = "as"
    items_per_user: int = 50


settings = Settings()
