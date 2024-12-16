import aiohttp
from src.app.errors.errors import HHAPIError
from src.app.schemas.auth import TokenResponse
from src.settings import Config


class HHAPIservice:

    AUTH_URL = "https://hh.ru/oauth/authorize"
    TOKEN_URL = "https://hh.ru/oauth/token"
    USERINFO_URL = "https://api.hh.ru/me"
    REDIRECT_URI = "http://localhost:8008/auth/callback"

    @staticmethod
    def get_auth_url(settings: Config):
        return (
            f'{HHAPIservice.AUTH_URL}?response_type=code'
            f'&client_id={settings.CLIENT_ID}'
            # f'state=123456'
            f'&redirect_uri=http://localhost:8008/auth/callback'
        )
    
    @staticmethod
    async def get_access_token(code: str, settings: Config) -> TokenResponse:
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
                HHAPIservice.TOKEN_URL,
                data=payload
            ) as response:
                if response.status != 200:
                    error_detail = await response.text()
                    raise HHAPIError(
                        f"Failed to fetch user info: {error_detail}",
                        status_code=response.status,
                    )
                response = await response.json()
                token = TokenResponse(**response)
                return token
            
    @staticmethod
    async def get_hh_user(token: TokenResponse):
        """Get user info from HH.ru

        Args:
            token (TokenResponse): _description_
        """
        header = {
                    'Authorization': f'Bearer {token.access_token}',
                    'HH-User-Agent': 'mu_requests (keldivad@gmail.com)'
                }
        async with aiohttp.ClientSession() as session:
            async with session.get(
                HHAPIservice.USERINFO_URL,
                headers=header
            ) as response:
                if response.status != 200:
                    error_detail = await response.text()
                    raise HHAPIError(
                        f"Failed to fetch user info: {error_detail}",
                        status_code=response.status,
                    )
                
                user_info = await response.json()
                return user_info


if __name__ == '__main__':
    # print(HHAPIservice.get_auth_url())
    # print(HHAPIservice.get_access_token('123456'))
    print(HHAPIservice.get_hh_user('USERHCF6CBTV431GI1AJFCE4O0ISD3CRC4AGVBMP7CF1BCB9378ES1BFSAGMK7MF'))