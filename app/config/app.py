from pydantic import BaseModel


class AppConfig(BaseModel):
    title: str = "0-project"
    host: str = "127.0.0.1"
    port = 8000
