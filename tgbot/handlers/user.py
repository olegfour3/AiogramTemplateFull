from aiogram.types import Message


async def user_start(message: Message):
    await message.reply("Hello, user!")

