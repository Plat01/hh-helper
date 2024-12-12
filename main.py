import asyncio
from src import bot

bot = bot.HHBot()

print(asyncio.run(bot.get_access_token()))