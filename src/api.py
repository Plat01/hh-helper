from fastapi import APIRouter

router = APIRouter()

@router.get('/')
async def index():
    return {'message': 'Hello World'}


@router.get('/auth')
async def auth():
    return {'message': 'Auth'}