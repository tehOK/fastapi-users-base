from pydantic import BaseModel, ConfigDict, Field
from pydantic_settings import BaseSettings


class RunSettings(BaseModel):
    host: str = Field(default="localhost")
    port: int = Field(default=8180)
    reload: bool = Field(default=True)


class DBSettings(BaseModel):
    db_url: str = Field(
        default="sqlite+aiosqlite:///./test_db.sqlite3",
    )
    echo: bool = Field(
        default=True,
    )

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class AccessTokenSettings(BaseModel):
    lifetime_seconds: int = Field(
        default=60 * 60 * 24 * 7,  # 7 days
    )
    reset_password_token_secret: str
    verification_token_secret: str


class Settings(BaseSettings):
    run: RunSettings = RunSettings()
    db: DBSettings = DBSettings()
    access_token: AccessTokenSettings
    model_config = ConfigDict(
        case_sensitive=False,
        env_file=".env",
        env_prefix="APP",
        env_nested_delimiter="__",
    )


settings = Settings()
