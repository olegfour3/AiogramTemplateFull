from contextlib import suppress

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageCantBeDeleted, MessageToDeleteNotFound

from loader import dp


async def delete_message(message: types.Message):
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await message.delete()


@dp.callback_query_handler(text='back_to_menu', state='*')
async def send_menu(call: CallbackQuery, state: FSMContext):
    try:
        await state.reset_state()
    except:
        pass




