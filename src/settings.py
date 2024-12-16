from functools import lru_cache
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join('..', '.env'))


class Config:
    CLIENT_ID = os.getenv('CLIENT_ID', default='fake_app')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    REDIRECT_URL = os.getenv('REDIRECT_URL')
    
    USER_EMAIL = os.getenv('USER_EMAIL')
    USER_PASSWORD = os.getenv('USER_PASSWORD')

@lru_cache()
def get_settings():
    return Config

if __name__ == '__main__':
    print(Config.CLIENT_ID, Config.CLIENT_SECRET)