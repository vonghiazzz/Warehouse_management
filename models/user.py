# models/user.py
import hashlib

class User:
    DEFAULT_USERNAME = "admin"
    DEFAULT_PASSWORD_HASH = hashlib.sha256("123456".encode()).hexdigest()

    @staticmethod
    def check_login(username: str, password: str) -> bool:
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        return (
            username == User.DEFAULT_USERNAME 
            and password_hash == User.DEFAULT_PASSWORD_HASH
        )
