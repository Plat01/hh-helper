from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse

from src.app.services.hh import HHAPIservice
from src.settings import Config, get_settings


router = APIRouter()

@router.get('/')
async def index():
    return {'message': 'Hello World'}

@router.get('/auth')
async def auth(settings: Config = Depends(get_settings)):
    """Redirect user to hh.ru OAuth page

    Returns:
        settings: Config
    """
    url = HHAPIservice.get_auth_url(settings=settings)
    return RedirectResponse(url=url)

@router.get('/auth/callback')
async def auth_callback(request: Request,
                        settings: Config = Depends(get_settings)):
    """Callback from hh.ru OAuth page

    Returns:
        request: Request
    """
    code = request.query_params.get('code')

    token = await HHAPIservice.get_access_token(code, settings=settings)
    resp = await HHAPIservice.get_hh_user(token)
    return resp
