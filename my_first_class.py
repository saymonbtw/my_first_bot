class User:
    def __init__(self, user_id: int, name: str, age: int, email: str):
        self.user_id = user_id
        self.name = name
        self.age = age
        self.email = email

    def get_user_info(user: User) -> str:
        return f"Возраст пользователя {user.name} - {user.age}\na email - {user.email}"


user_1 = User(42, "Semen", 20, "coolmansemen@gmail.com")
print(user_1.get_user_info())

user_2 = User(2, "Luba", 19, "luba26@gmail.com")
print(user_2.get_user_info())
