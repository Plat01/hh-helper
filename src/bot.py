import aiohttp 

from src.settings import Config

class HHBot:

    def __init__(self):
        self.client_id = Config.CLIENT_ID
        self.client_secret = Config.CLIENT_SECRET
        self.redirect_url = Config.REDIRECT_URL

    async def get_access_token(self, request):
        code = request.query.get('code')
        if not code:
            return aiohttp.web.Response(text="Authorization code not found", status=400)

        # Exchange authorization code for access token
        async with aiohttp.ClientSession() as session:
            data = {
                'grant_type': 'authorization_code',
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'code': code,
                'redirect_uri': self.redirect_url
            }
            async with session.post('https://hh.ru/oauth/token', data=data) as response:
                token_response = await response.json()
                return aiohttp.web.Response(text=f"Access Token: {token_response.get('access_token')}")

    # async def get_access_token(self):
    #     request_url = 
    #     params = {
    #         'grant_type': 'client_credentials',
    #         'client_id': self.client_id,
    #         'client_secret': self.client_secret
    #     }

    #     async with aiohttp.ClientSession() as session:
    #         request = await session.post(request_url, params=params)
    #         return await request.json()