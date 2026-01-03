from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    name: str
    age: int
    email: str

    def get_user_info(user: User) -> str:
        return f"Возраст пользователя {user.name} - {user.age}\na email - {user.email}"


user_1 = User(26, "Inav", 15, "rassh@gmail.com")
print(user_1.get_user_info())
