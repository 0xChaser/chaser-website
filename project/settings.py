from enum import Enum
from functools import lru_cache

from pydantic import (EmailStr, Field, MariaDBDsn, MySQLDsn, PostgresDsn,SecretStr)
from pydantic_settings import BaseSettings, SettingsConfigDict

class LogLevel(str, Enum):
    critical = "critical"
    error = "error"
    warning = "warning"
    info = "info"
    debug = "debug"
    trace = "trace"


class Settings(BaseSettings):
    database_uri: PostgresDsn | MySQLDsn | MariaDBDsn
    pgadmin_email: EmailStr
    pgadmin_password: SecretStr
    secret_key: SecretStr
    algorithm: str
    access_token_expire_minutes: int
    date_format: str

    host: str = "127.0.0.1"
    port: int = Field(default=8090, gt=0, lt=65535)
    workers: int | None = None
    proxy_headers: bool = False
    log_level: LogLevel = LogLevel.info

    model_config = SettingsConfigDict(env_file=(".env", ".env.local", ".env.prod"), extra="ignore")


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
