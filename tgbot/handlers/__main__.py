from aiogram import types, Dispatcher
from .admin import admin_start
from .user import user_start, user_help
from .echo import bot_echo, bot_echo_all
from .errors import message_not_modified, message_to_delete_not_found
from aiogram.utils import exceptions


def register_all_handlers(dp):
    register_admin(dp)
    register_user(dp)
    register_errors(dp)

    register_echo(dp)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(user_help, commands=["help"], state="*")


def register_errors(dp: Dispatcher):
    dp.register_errors_handler(message_not_modified, exception=exceptions.MessageNotModified)
    dp.register_errors_handler(message_to_delete_not_found, exception=exceptions.MessageToDeleteNotFound)


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo)
    dp.register_message_handler(bot_echo_all, state="*", content_types=types.ContentTypes.ANY)