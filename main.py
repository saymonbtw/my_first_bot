import os
from dataclasses import dataclass


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


token = os.getenv("BOT_TOKEN")
admin_id = int(os.getenv("ADMIN_ID"))


bot = TgBot(token=token, admin_ids=admin_id)
