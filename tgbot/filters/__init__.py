from .IsAdminFilter import IsAdmin
from .FiltersChat import IsPrivate
from loguru import logger


def register_all_filters(dp):
    logger.info("Подключение filters...")
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsPrivate)