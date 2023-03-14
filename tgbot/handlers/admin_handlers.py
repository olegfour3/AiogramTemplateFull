from aiogram import types
from asyncio import sleep
from loguru import logger

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.markdown import escape_md
from aiogram.dispatcher import FSMContext
from loader import dp, bot


@dp.message_handler(is_admin=True, commands=['start', 'admin'])
async def admin_start(message: types.Message):
    await message.answer("Привет, админ!")



