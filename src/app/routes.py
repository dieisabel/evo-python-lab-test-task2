__all__ = ['router']

from typing import Dict
from typing import Any

from fastapi import Request
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from dependencies import Templates
from entities import UserData
from services import IUserDataService
from services import UserDataService

router: APIRouter = APIRouter()
service: IUserDataService = UserDataService()
templates: Jinja2Templates = Templates()


@router.get('/', response_class=HTMLResponse)
def index(request: Request) -> Any:
    return templates.TemplateResponse('index.html', {'request': request})


@router.get('/all_user_data', response_class=HTMLResponse)
def all_user_data(request: Request) -> Any:
    return templates.TemplateResponse('all_user_data.html', {
        'request': request,
        'all_user_data': service.find_all(),
    })


@router.post('/api/user_data')
def add_user_data(user_data: UserData) -> Dict[str, bool]:
    return {'status': service.add(user_data)}
