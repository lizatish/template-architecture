from functools import lru_cache

from core.config import get_settings
from models.general import OutputModel, InputModel
from src.db.test_db_repository import get_test_db_repository, TestDBRepository

conf = get_settings()


class Service:

    def __init__(self, db_repository: TestDBRepository):
        """Инициализация сервиса."""
        self.db_repository = db_repository

    async def test_service_logic(self, init_model: InputModel) -> OutputModel:
        # await self.db_repository.get_db_data()
        return OutputModel(**init_model.model_dump(), name="name", number=1)


@lru_cache()
def get_service(
) -> Service:
    return Service(db_repository=get_test_db_repository())
