
from src.model.repository import UsersRepository

class CreateUserController:

    def create_user(name: str, email: str, password: str, confirm: str) -> None:

        if len(password) < 5 and len(password) > 20:
            response = {"status": "error", "message": "The password must be at least 5 characters and no more than 20 characters long"}
        
        elif password != confirm:
            response = {"status": "error", "message": "Password and password confirmation are different"}

        elif email.count("@") != 1:
            response = {"status": "error", "message": "The format for email is invalid"}
        
        elif len(name) < 5:
            response = {"status": "error", "message": "The name must be at least 5 characters long"}
        
        else:

            request = UsersRepository().insert(name=name, email=email, password=password, admin=True)

            if not request:
                response = {"status": "error", "message": "Error trying to register user" }
            
            else: 
                response = {"status": "success", "message": "Successfully registered"}

        return response
