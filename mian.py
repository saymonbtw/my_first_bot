import os
from dataclasses import dataclass
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).with_name("bot_info.env"))


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


token = os.getenv("BOT_TOKEN")
admin_ids = list(map(int, os.getenv("ADMIN_IDS").split(",")))

if not token or not admin_ids:
    raise RuntimeError("ошибка чтения файла с данными бота")

bot = TgBot(token=token, admin_ids=admin_ids)
print(bot)
