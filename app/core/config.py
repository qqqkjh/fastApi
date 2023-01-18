from typing import Any, Dict, List, Optional, Union
from pydantic import BaseSettings, validator, PostgresDsn
from dotenv import load_dotenv
from app.utils.path import get_env_path

load_dotenv(get_env_path())


class EnvConfig(BaseSettings):
    ENVIRONMENT: str = "local"


env_config = EnvConfig()


def set_evn(evn_name: str):
    if evn_name == "local":
        evn = f".env.{evn_name}"
        load_dotenv(get_env_path(evn))


set_evn(env_config.ENVIRONMENT)


class Settings(BaseSettings):
    POSTGRES_SERVER: str = None
    POSTGRES_USER: str = None
    POSTGRES_PASSWORD: str = None
    POSTGRES_DB: str = None
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )


settings = Settings()
