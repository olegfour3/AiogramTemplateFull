from aiogram import types, Dispatcher
from .admin import admin_start
from .user import user_start
from .echo import bot_echo, bot_echo_all

def register_all_handlers(dp):
    register_admin(dp)
    register_user(dp)

    register_echo(dp)

def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo)
    dp.register_message_handler(bot_echo_all, state="*", content_types=types.ContentTypes.ANY)