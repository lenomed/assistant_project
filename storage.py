import json
from user import User


class Storage:

    def save_user(self, user: User):
        # Load existing data safely
        try:
            with open('user_data.json', 'r') as file:
                data = json.load(file)

                # Fix corrupted file automatically
                if not isinstance(data, list):
                    data = []

        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        # Check if user exists
        for existing_user in data:
            if existing_user["name"] == user.name:
                print("User already exists")
                return

        # Add new user
        new_user = {
            "name": user.name,
            "age": user.age,
            "email": user.email,
            "nickname": user.nickname,
            "score": user.score
        }

        data.append(new_user)

        # Save back to file
        with open('user_data.json', 'w') as file:
            json.dump(data, file, indent=4)

        print("User saved successfully")

    def load_user(self, name,email):
        try:
            with open('user_data.json', 'r') as file:
                data = json.load(file)

                if not isinstance(data, list):
                    return None

                for user in data:
                    if user["name"] == name and user["email"].lower() == email:
                        return User(
                            user["name"],
                            user["age"],
                            user["email"],
                            user["nickname"],
                            user["score"]
                        )
                    else:
                        user = []
                    print("User not found")
                    return None

        except FileNotFoundError:
            print("File does not exist")
            return None

    def get_all_users(self):
        try:
            with open('user_data.json', 'r') as file:
                data = json.load(file)
                print("\n".join(f"{u['name']} is {u['age']}, {u['email']}, {u['nickname']}, {u['score']}" for u in data))
                return data if isinstance(data, list) else []
        except FileNotFoundError, json.JSONDecodeError:
            return []
