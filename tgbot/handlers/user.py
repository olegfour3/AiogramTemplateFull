from aiogram.types import Message
from tgbot.misc import rate_limit


@rate_limit(5, 'start')
async def user_start(message: Message):
    await message.reply("Hello, user!")


@rate_limit(5, 'help')
async def user_help(message: Message):
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/help - Получить справку'
    ]
    await message.answer('\n'.join(text))
