import os
from dataclasses import dataclass
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).with_name(".env"))


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


token = os.getenv("BOT_TOKEN")
admin_id = os.getenv("ADMIN_ID")

if not token or not admin_id:
    raise RuntimeError("ошибка чтения файла с данными бота")

bot = TgBot(token=token, admin_ids=admin_id)
print(bot)
