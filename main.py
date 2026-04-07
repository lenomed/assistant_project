from user import User
from storage import Storage

name = User.input_name()
age = User.input_age()

user1 = User(name, age)

user1.generate_nickname()
user1.add_score(50)

storage = Storage()

storage.save_user(user1)

loaded_user = storage.load_user(name)


if loaded_user:
    print(f"Loaded User:, User Name: {loaded_user.get_name()}, User Score:{loaded_user.get_score()}")