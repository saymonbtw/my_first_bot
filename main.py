from dataclasses import dataclass


@dataclass
class TgBot:
    token: str
    admin_id: list[int]


bot = TgBot("8507449795:AAEmUJNNu0SnLzzKdDWIhHBWh4nBWmVQ_1o", [835613839])
