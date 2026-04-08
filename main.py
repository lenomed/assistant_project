import json
from user import User
from storage import Storage
from cli import Command

name = User.input_name()
age = User.input_age()
email = User.input_email()



def main():
    app = Command()
    app.run()


if __name__ == "__main__":
    main()



try:
    with open('user_data.json', 'r') as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    data = []

user_exists= any(u.get("name", "").lower() == name.lower() for u in data)
has_email = any(e.get("email", "").lower() == email.lower() for e in data)



if user_exists or has_email:
        print("Welcome back")


user1 = User(name, age, email)

user1.generate_nickname()
user1.add_score(50)

storage = Storage()

storage.save_user(user1)

net_users = storage.get_all_users()
print(net_users)

loaded_user = storage.load_user(name,email)


if loaded_user:
    print("=" * 40)
    print(f"Loaded User:, "
          f"User Name: {loaded_user.get_name()},\n" 
          f"User Score:{loaded_user.get_score()}\n"
          f"your email is:{email} \n")
    print("=" * 40)