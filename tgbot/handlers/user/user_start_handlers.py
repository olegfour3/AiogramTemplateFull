from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from tgbot.database import db_commands
from tgbot.filters import IsPrivate


@dp.message_handler(IsPrivate(), CommandStart(), state='*')
async def register_user(message: types.Message):
    await message.answer("Привет")
