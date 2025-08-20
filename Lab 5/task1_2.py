from cryptography.fernet import Fernet
import os

def load_or_create_key(key_path: str = "secret.key") -> bytes:
    if os.path.exists(key_path):
        with open(key_path, "rb") as key_file:
            return key_file.read()
    key = Fernet.generate_key()
    with open(key_path, "wb") as key_file:
        key_file.write(key)
    return key

def collect_and_save_student_details():
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    email = input("Enter student's Email: ")
    details = f"Name: {name}, Age: {age}, Email: {email}"
    key = load_or_create_key()
    fernet = Fernet(key)
    token = fernet.encrypt(details.encode("utf-8"))
    with open("student_details.txt", "w") as file:
        file.write(token.decode("utf-8"))
        print("Encrypted student details saved successfully.")
if __name__ == "__main__":
    collect_and_save_student_details()