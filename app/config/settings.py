from typing import Literal

from pydantic import Field
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

from app.config.app import AppConfig
from app.config.constants import BASE_DIR


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=BASE_DIR / ".env",
        env_nested_delimiter="__",
    )

    env: Literal["dev", "test", "prod"] = "dev"
    app: AppConfig = Field(default_factory=AppConfig)


settings = Settings()
