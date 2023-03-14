import logging
import locale

from aiogram import executor

from tgbot.filters import register_all_filters
from tgbot.middlewares import register_all_middlewares

from tgbot.utils.notify_admins import AdminNotification
from tgbot.utils.set_bot_commands import set_default_commands

from loader import dp, db, bot
from config import load_config


logger = logging.getLogger(__name__)

locale.setlocale(
    category=locale.LC_ALL,
    locale="Russian"
)


logging.basicConfig(
    level=logging.DEBUG if load_config().misc.debug else logging.INFO,
    format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
)


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    # Уведомляет о запуске
    await AdminNotification.send(dispatcher)

    #TODO: если есть БД, то проверяем подключение к ней

    # logging.info(f'Создаем подключение...')
    # await db.create()
    # logging.info(f'Подключение успешно!')
    # logging.info(f'База загружена успешно!')


async def on_shutdown(dispatcher):
    await AdminNotification.send(dispatcher, startup=False)


def start_bot():
    try:
        logger.info("Запуск бота")

        bot['config'] = load_config()

        register_all_middlewares(dp, load_config())
        register_all_filters(dp)
        import tgbot.handlers

        executor.start_polling(dispatcher=dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)

    except (KeyboardInterrupt, SystemExit):
        logger.error("Бот остановлен!")


if __name__ == '__main__':
    start_bot()
