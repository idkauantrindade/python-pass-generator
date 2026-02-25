import json
import secrets
import string
from datetime import datetime
import os

FILE_NAME = "passwords.json"

def init_json():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump([], f)

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

def save_password(password, tag):
    with open(FILE_NAME, "r") as f:
        history = json.load(f)

    history.append({
        "password": password,
        "tag": tag,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    with open(FILE_NAME, "w") as f:
        json.dump(history, f, indent=4)

def show_history():
    with open(FILE_NAME, "r") as f:
        history = json.load(f)

    if history:
        print("\n--- Password History ---")
        for idx, item in enumerate(reversed(history), 1):
            print(f"{idx}. Password: {item['password']} | Tag: {item['tag']} | Created at: {item['created_at']}")
    else:
        print("\nNo passwords generated yet.")

def main():
    init_json()
    while True:
        print("\n1 - Generate new password")
        print("2 - View password history")
        print("3 - Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            length = input("Password length (default 12): ")
            length = int(length) if length.isdigit() else 12
            password = generate_password(length)
            print(f"\nGenerated password: {password}")
            tag = input("Enter a tag/description: ")
            save_password(password, tag)
            print("Password saved successfully!")
        elif choice == "2":
            show_history()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
