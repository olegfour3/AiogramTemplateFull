from aiogram import Dispatcher
from tgbot.middlewares.environment import EnvironmentMiddleware


def register_all_middlewares(dp, config):
    dp.setup_middleware(EnvironmentMiddleware(config=config))