__all__ = ['create_application']

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes import router


def create_application() -> FastAPI:
    application: FastAPI = FastAPI()
    application.mount('/static', StaticFiles(directory='./../static'), name='static')
    application.include_router(router)
    return application
