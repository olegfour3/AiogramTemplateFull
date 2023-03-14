from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from config import load_config
from tgbot.database.db_main import Database

bot = Bot(token=load_config().tg_bot.token, parse_mode=types.ParseMode.HTML)
storage = RedisStorage2() if load_config().tg_bot.use_redis else MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database()


