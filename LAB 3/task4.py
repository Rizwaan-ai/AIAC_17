# Simple user registration and login system using linked functions

users_db = {}

def register_user():
    print("\n--- User Registration ---")
    username = input("Enter a username: ").strip()
    if username in users_db:
        print("Username already exists. Please try a different username.")
        return
    password = input("Enter a password: ").strip()
    users_db[username] = password
    print("Registration successful! You can now log in.")

def login_user():
    print("\n--- User Login ---")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    if username in users_db and users_db[username] == password:
        print(f"Login successful! Welcome, {username}.")
    else:
        print("Invalid username or password. Please try again.")

def main():
    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()
        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
