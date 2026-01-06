import os
from dataclasses import dataclass
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).with_name("bot_info.env"))


@dataclass
class DatabaseConfig:
    host: str  # адрес БД
    user: str  # имя пользователя БД
    password: str  # пароль от БД
    database: str  # название БД


@dataclass
class TgBot:
    token: str  # токен бота
    admin_ids: list[int]  # список id админов


@dataclass
class Config:
    bot: TgBot
    db: DatabaseConfig


token = os.getenv("BOT_TOKEN")
admins = os.getenv("ADMIN_IDS")

if not token or not admins:
    raise RuntimeError("ошибка чтения файла с данными бота")

admins = [int(x.strip()) for x in admins.split(",")]

bot = TgBot(token=token, admin_ids=admins)

db = DatabaseConfig(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
)

if not all([db.host, db.user, db.password, db.database]):
    raise RuntimeError("ошибка чтения данных БД")

config = Config(bot=bot, db=db)
finally
