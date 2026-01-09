from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field
from pydantic_settings import BaseSettings


class RunSettings(BaseModel):
    host: str = Field(default="localhost")
    port: int = Field(default=8180)
    reload: bool = Field(default=True)


class Settings(BaseSettings):
    run: RunSettings = RunSettings()

    model_config = ConfigDict(
        case_sensitive=False,
        env_file=".env",
        env_prefix="APP_",
        env_nested_delimiter="__",
    )


settings = Settings()
