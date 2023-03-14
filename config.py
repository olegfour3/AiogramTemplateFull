from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import List
from environs import Env


@dataclass
class DataBaseConfig:
    user: str
    password: str
    host: str
    database: str


@dataclass
class TgBot:
    token: str
    admin_ids: List[int]
    use_redis: bool


@dataclass
class Miscellaneous:

    debug: bool
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    db: DataBaseConfig
    misc: Miscellaneous


@lru_cache
def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            use_redis=env.bool("USE_REDIS"),
        ),
        db=DataBaseConfig(
            user=env.str('DB_USER'),
            password=env.str('DB_PASS'),
            host=env.str('DB_HOST'),
            database=env.str('DB_NAME'),
        ),
        misc=Miscellaneous(
            debug=env.bool("DEBUG"),
        )
    )


BASE_DIR = Path(__file__).parent
