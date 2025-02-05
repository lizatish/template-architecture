from fastapi import APIRouter, Depends

from src.models.general import OutputModel, InputModel
from src.service import get_service, Service

router = APIRouter()


@router.post('/test_route', response_model=OutputModel)
async def test_route(init_model: InputModel, service: Service = Depends(get_service)) -> OutputModel:
    return await service.test_service_logic(init_model)
