from user import User
from storage import Storage

class Command:

    def __init__(self):
        self.storage = Storage()


    def show_menu(self):
        print("\n" + "=" * 55)
        print("           USER MANAGEMENT SYSTEM")
        print("=" * 55)
        print("1. Create New User")
        print("2. Find User by Name")
        print("3. Show All Users")
        print("4. Exit")
        print("=" * 55)

    def create_new_user(self):
        print('======= create new user =======')
        name = User.input_name()
        age = User.input_age()
        email = User.input_email()

        user = User(name, age, email)

        user.generate_nickname()
        user.add_score(50)



        self.storage.save_user(user)

        print("\n✅ User created and saved successfully!")
        self.display_user_info(user)

    def find_user(self):
        print("\n--- Find User ---")
        name = input("Enter name to search: ").strip().lower()

        if not name:
            print("Name cannot be empty.")
            return

        email = input("Enter email: ").strip().lower()
        user = self.storage.load_user(name, email)

        if user:
            print("\n✅ User Found!")
            self.display_user_info(user)
        else:
            print(f"❌ No user found with the name '{name}'.")

    def show_all_users(self):
        users_data = self.storage.get_all_users()

        if not users_data:
            print("No users found in the database.")
            return

        print("\n--- All Users ---")
        print(f"{'Name':<15} {'Email':<25} {'Nickname':<15} {'Score':<6}")
        print("-" * 65)

        for u in users_data:
            print(f"{u.get('name', 'N/A'):<15} "
                  f"{u.get('email', 'N/A'):<25} "
                  f"{u.get('nickname', 'N/A'):<15} "
                  f"{u.get('score', 0):<6}")

    def display_user_info(self, user: User):
        """Helper method to display user nicely"""
        print(f"Name     : {user.get_name()}")
        print(f"Age      : {user.get_age()}")
        print(f"Nickname : {user.get_nickname() or 'Not generated'}")
        print(f"Email    : {user.get_email()}")
        print(f"Score    : {user.get_score()}")

    def run(self):
        print("Welcome to User Management System!")

        while True:
            self.show_menu()
            choice = input("\nEnter your choice (1-4): ").strip()

            if choice == "1":
                self.create_new_user()
            elif choice == "2":
                self.find_user()
            elif choice == "3":
                self.show_all_users()
            elif choice == "4":
                print("\nThank you for using the User Management System. Goodbye!")
                break
            else:
                print("Invalid option! Please choose a number between 1 and 4.")

        if __name__ == "__main__":
            cline = Command()
            cline.run()

    @staticmethod
    def look_up_age(self):
        pass