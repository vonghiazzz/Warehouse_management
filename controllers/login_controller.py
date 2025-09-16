from models.user import User

class LoginController:
    @staticmethod
    def authenticate(username, password):
        
        return User.check_login(username, password)