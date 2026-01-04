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
admin_raw = os.getenv("ADMIN_IDS")

if not token or not admin_raw:
    raise RuntimeError("ошибка чтения файла с данными бота")

admin_raw = [int(x) for x in admin_raw.split(",")]

bot = TgBot(token=token, admin_ids=admin_raw)
print(bot)
