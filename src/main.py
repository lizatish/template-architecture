from contextlib import asynccontextmanager

import uvicorn as uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.api import routes
from src.core.config import get_settings
from src.core.logger import setup_root_logger
from src.db.db_factory import init_session, get_session

conf = get_settings()

app = FastAPI(
    title=conf.PROJECT_NAME,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_root_logger()
    await init_session()
    yield
    session = await get_session()
    await session.close()


app.include_router(routes.router, prefix='/api/v1/test', tags=['test'])

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        log_level=conf.LOG_LEVEL
    )
