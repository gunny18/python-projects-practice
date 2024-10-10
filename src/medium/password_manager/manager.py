import os
from pathlib import Path
from cryptography.fernet import Fernet


DIR_PATH = Path(__file__).parent.resolve()


def create_key():
    pth = os.path.join(DIR_PATH, "key.key")
    key = Fernet.generate_key()
    if not os.path.exists(pth):
        with open(pth, "wb") as f:
            f.write(key)
    else:
        print("Key already exists")


def load_key():
    pth = os.path.join(DIR_PATH, "key.key")
    key = None
    with open(pth, "rb") as f:
        key = f.read()
    return key


class PasswordManager:

    allowed_modes = {"add", "view", "quit"}
    pwd_file = os.path.join(DIR_PATH, "passwords.txt")

    def __init__(self) -> None:
        self.master_pwd = None

    def add(self, fer: Fernet):
        usn = input("Enter username: ")
        pwd = input("Enter password: ")
        enc_pwd = fer.encrypt(pwd.encode()).decode()
        with open(PasswordManager.pwd_file, "a") as f:
            f.write(f"{usn}|{enc_pwd}\n")

    def view(self, fer: Fernet):
        with open(PasswordManager.pwd_file, "r") as f:
            for entry in f.readlines():
                usn, pwd = entry.split("|")
                dec_pwd = fer.decrypt(pwd.encode()).decode()
                print(f"Username: {usn} | Password: {dec_pwd}")

    def start(self):
        self.master_pwd = self.prompt_master_password()
        create_key()
        key = load_key()
        fer = Fernet(key)
        while True:
            mode = self.prompt_mode()
            if mode not in PasswordManager.allowed_modes:
                print("Invalid mode")
                continue

            if mode == "quit":
                break
            elif mode == "add":
                self.add(fer)
            else:
                self.view(fer)

    def prompt_mode(self):
        mode = input("Enter mode [add/view/quit]: ")
        return mode

    def prompt_master_password(self):
        p = input("Enter master password: ")
        return p
