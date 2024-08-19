import os

from dotenv import load_dotenv

# load_dotenv(dotenv_path=os.path.join('..', '.env'))
load_dotenv()


GITHUB_CLIENT_TOKEN = os.getenv('GITHUB_CLIENT_TOKEN')
GITHUB_APP_TOKEN = os.getenv('GITHUB_APP_TOKEN', default='fake_app')

if __name__ == '__main__':
    print(GITHUB_CLIENT_TOKEN)
