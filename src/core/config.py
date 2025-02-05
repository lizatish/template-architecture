from __future__ import annotations

import logging
from functools import lru_cache

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Настройки приложения."""

    LOG_LEVEL: int = logging.DEBUG

    SERVICE_HOST: str = 'service'
    SERVICE_PORT: int = 4555

    DATABASE_URL: str = 'postgresql+asyncpg://postgres:password@localhost:5433/data'
    SQLALCHEMY_POOL_SIZE: int = 30
    SQLALCHEMY_MAX_OVERFLOW: int = 0

    # Название проекта. Используется в Swagger-документации
    PROJECT_NAME: str = 'Test Project Name'

    class Config:
        """Дополнительные базовые настройки."""

        env_file = '.env'
        env_file_encoding = 'utf-8'


@lru_cache
def get_settings():
    """Возвращает настройки тестов."""
    return Settings()
