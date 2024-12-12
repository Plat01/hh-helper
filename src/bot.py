import aiohttp 

from src.settings import Config

class HHBot:

    def __init__(self):
        self.client_id = Config.CLIENT_ID
        self.client_secret = Config.CLIENT_SECRET
        self.redirect_url = Config.REDIRECT_URL

        self.user_email = Config.USER_EMAIL
        self.user_password = Config.USER_PASSWORD

    async def get_access_token(self):

        async with aiohttp.ClientSession() as session:
            data = {
                'grant_type': 'password',
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'username': self.user_email,
                'password': self.user_password
            }
            TOKEN_URL = 'https://hh.ru/oauth/token'
            
            async with session.post(TOKEN_URL, data=data) as response:
                if response.status == 200:
                    token_response = await response.json()
                    print("Access Token:", token_response.get('access_token'))
                    print("Refresh Token:", token_response.get('refresh_token'))
                else:
                    print("Error:", response.status, await response.text())