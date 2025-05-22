from src.WEB.model.repository import UsersRepository
from src.WEB.model.config import ConnectionMysqlDB

class CreateUserController:

    def create_user(self, name: str, email: str, password: str, confirm_password: str) -> dict:

        if not self.__validate_email(email):
            response = {"status": "error", "message": "O formato do email é inválido!"}

        elif not self.__validate_email_exists(email):
            response = {"status": "error", "message": "Email já cadastrado!"}

        elif not self.__validate_password(password):
            response = {"status": "error", "message": "A senha precisa ter entre 5 e 20 caracteres!"}

        elif not self.__validate_confirm_password(password, confirm_password):
            response = {"status": "error", "message": "As senhas precisam ser iguais!"}

        
        elif not self.__validate_name(name):
            response = {"status": "error", "message": "O nome de usuário precisa ter entre 5 e 100 caracteres!"}
        
        else:

            request = UsersRepository(ConnectionMysqlDB()).insert(name=name, email=email, password=password, admin=False)

            if not request:
                response = {"status": "error", "message": "Erro ao tentar registrar usuário!" }
            
            else: 
                response = {"status": "success", "message": "Registro feito com sucesso"}

        return response
    
    def __validate_email(self, email: str) -> bool:

        if email.count("@") != 1 or email.count(".") < 1:
            return False
        
        return True
    
    def __validate_email_exists(self, email:str) -> bool:

        request = UsersRepository(ConnectionMysqlDB()).select_by_email(email=email)

        if request:
            return False
        
        return True
        

    def __validate_password(self, password:str) -> bool:

        if len(password) < 5 or len(password) > 20:
            return False
        

        return True
    
    def __validate_confirm_password(self, password: str, confirm_password: str) -> bool:
        
        if password != confirm_password:
            return False
        
        return True
    
    def __validate_name(self, name: str) -> bool:

        if len(name) < 5 or len(name) > 100:
            return False  
        
        return True
