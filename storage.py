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
            "nickname": user.nickname,
            "score": user.score
        }

        data.append(new_user)

        # Save back to file
        with open('user_data.json', 'w') as file:
            json.dump(data, file, indent=4)

        print("User saved successfully")

    def load_user(self, name):
        try:
            with open('user_data.json', 'r') as file:
                data = json.load(file)

                if not isinstance(data, list):
                    return None

                for user in data:
                    if user["name"] == name:
                        return User(
                            user["name"],
                            user["age"],
                            user["nickname"],
                            user["score"]
                        )

                print("User not found")
                return None

        except FileNotFoundError:
            print("File does not exist")
            return None