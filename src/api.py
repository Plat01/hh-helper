from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse

from src.app.services.auth import Auth
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
    url = Auth.get_auth_url(settings=settings)
    return RedirectResponse(url=url)

@router.get('/auth/callback')
async def auth_callback(request: Request,
                        settings: Config = Depends(get_settings)):
    """Callback from hh.ru OAuth page

    Returns:
        request: Request
    """
    code = request.query_params.get('code')

    resp = await Auth.get_access_token(code, settings=settings)
    return resp
