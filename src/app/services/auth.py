import aiohttp
from src.app.schemas.auth import TokenResponse
from src.settings import Config


class Auth:

    AUTH_URL = "https://hh.ru/oauth/authorize"
    TOKEN_URL = "https://hh.ru/oauth/token"
    REDIRECT_URI = "http://localhost:8008/auth/callback"

    @staticmethod
    def get_auth_url(settings: Config):
        return (
            f'{Auth.AUTH_URL}?response_type=code'
            f'&client_id={settings.CLIENT_ID}'
            # f'state=123456'
            f'&redirect_uri=http://localhost:8008/auth/callback'
        )
    
    @staticmethod
    async def get_access_token(code: str, settings: Config):
        """Get access token and save it to database

        Args:
            code (str): _description_
            settings (Config): _description_

        Returns:
            _type_: _description_
        """

        payload = {
            'grant_type': 'authorization_code',
            'code': code,
            'client_id': settings.CLIENT_ID,
            'client_secret': settings.CLIENT_SECRET,
            # 'redirect_uri': 'http://localhost:8008/auth/success'
            'redirect_uri': 'http://localhost:8008/auth/callback'

        }

        async with aiohttp.ClientSession() as session:
            async with session.post(
                Auth.TOKEN_URL,
                data=payload
            ) as response:
                response = await response.json()
                token = TokenResponse(**response)
                return token
    