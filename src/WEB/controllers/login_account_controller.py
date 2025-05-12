from src.WEB.model.repository import UsersRepository
from src.WEB.model.config import ConnectionMysqlDB
from src.WEB.model.entities import Users


class LoginAccountController:

    def login_account(self, email:str, password:str) -> dict:

        user = UsersRepository(ConnectionMysqlDB()).select_by_email(email=email)

        if not self.__validate_inputs(email, password):
            response = {"status": "error", "message": "Preencha todos os campos!"}

        elif user is None:
            response = {"status": "error", "message": "Erro ao tentar logar na conta!"}

        elif user is False or not self.__validate_password(password, user):
            response = {"status": "error", "message": "Email ou senha incorretos!"}

        elif self.__validate_user_status(user):
            response = {"status": "error", "message": "Email ou senha incorretos!"}

        else:
            response = {"status": "success", "message": "Logado com sucesso!"}
    
        return response

    def __validate_password(self, password: str, user: Users) -> bool:

        if user.user_password != password:
            return False
        
        return True
    
    def __validate_inputs(self, email: str, password: str) -> bool:

        if not email or not password:
            return False
        
        return True
    
    def __validate_user_status(self, user: Users) -> bool:
        return int(user.user_status) == 0
        
