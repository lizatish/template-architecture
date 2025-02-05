from functools import lru_cache

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.db_factory import get_session


class TestDBRepository:
    def __init__(self, session: AsyncSession):
        """Инициализация сервиса."""
        self.session = session

    async def get_db_data(self):
        pass


@lru_cache()
def get_test_db_repository(
        session: AsyncSession = Depends(get_session)
) -> TestDBRepository:
    return TestDBRepository(session)
