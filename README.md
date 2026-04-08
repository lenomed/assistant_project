assitant_project/
│
├── main.py        # Entry point of the application
├── cli.py         # Command-line interface (menu system)
├── user.py        # User class (data & logic)
├── storage.py     # Handles saving/loading users (JSON)
├── user_data.json # Database file

git clone https://github.com/lenomed/assitant_project.git
cd assitant_project
python main.py

🧪 How It Works
The user interacts with a CLI menu.
Input is collected (name, age, email).
A User object is created.
A nickname is randomly generated.
The user is saved to a JSON file.
Data can be retrieved, displayed, or searched.

📂 Data Storage

Users are stored in a JSON file (user_data.json) in the following format:

[
  {
    "name": "john",
    "age": 25,
    "email": "john@example.com",
    "nickname": "ShadowX",
    "score": 50
  }
]

🧠 Concepts Used
Object-Oriented Programming (Classes & Objects)
File Handling (with open)
JSON Serialization (json.dump, json.load)
Error Handling (try/except)
CLI Design (menu-driven apps)

🔮 Future Improvements
🔐 Login system (email-based authentication)
✏️ Update user details
🗑️ Delete users
🏆 Leaderboard (top scores)
🌐 Convert to web app (Flask/Django)

👨‍💻 Author

Built by [Sunday Ohabuenyi]
Feel free to fork, improve, and contribute!

License

This project is open-source and available
