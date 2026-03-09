from typing import Literal

from pydantic import Field
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

from app.config.app import AppConfig
from app.config.constants import ENVS_DIR
from app.config.database import DatabaseConfig
from app.config.logging import LoggingConfig


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_file=(
            ENVS_DIR / ".env.template",
            ENVS_DIR / ".env",
        ),
        env_nested_delimiter="__",
    )

    env: Literal["dev", "test", "prod"] = "dev"
    app: AppConfig = Field(default_factory=AppConfig)
    logging: LoggingConfig = Field(default_factory=LoggingConfig)
    db: DatabaseConfig = Field(default_factory=DatabaseConfig)


settings = Settings()
