import typing

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from config import load_config


class IsAdmin(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin: typing.Optional[bool] = None):
        self.is_admin = is_admin

    async def check(self, message: types.Message):
        if self.is_admin is None:
            return False
        return True if message.from_user.id in load_config().tg_bot.admin_ids else False

