from src.WEB.model.repository import GamesRepository, UsersRepository, GameRentalRepository
from src.WEB.model.config import ConnectionMysqlDB
from src.WEB.model.entities import Users, Games, GameRental


class InsertController():

    def insert_game(self, name: str, price:str, quantity:str, genre: str, description: str) ->dict:

        if self.__validate_required_fields(name):
            return {"status": "error", "message": "O campo com nome do jogo precisa ser preenchido!"}
        
        if self.__validate_required_fields(price):
            return {"status": "error", "message": "O campo com preço do jogo precisa ser preenchido!"}
        
        if self.__validate_required_fields(quantity):
            quantity = "0"

        if self.__validate_string_to_float_conversion(price):
            return {"status": "error", "message": "Preço precisa ser um número!"}
               
        if self.__validate_string_to_integer_conversion(quantity):
            return {"status": "error", "message": "Quantidade precisa ser um número!"}
        
        if self.__validate_string_limit(name, 100):
            return {"status": "error", "message": "O nome do jogo precisa ter menos de 100 caracteres!"}
        
        if self.__validate_string_limit(genre, 100):
            return {"status": "error", "message": "O gênero do jogo precisa ter menos de 100 caracteres!"}
        
        name = name.strip()
        price = float(price)
        quantity = int(quantity)
        genre = genre.strip()
        description = description.strip()

        repository = GamesRepository(ConnectionMysqlDB())
        request =repository.insert(name=name, price=price, quantity=quantity, genre=genre, description=description)

        if not request:
            return {"status": "error", "message": "Erro ao tentar registrar jogo no banco de dados!"}
        
        return {"status": "success", "message": "Jogo registrado com sucesso!"}
    

    def insert_user(self, name: str, email: str, password: str, confirm_password: str, admin: str) -> dict:

        if self.__validate_required_fields(name):
            return {"status": "error", "message": "O campo com nome do usuário precisa ser preenchido!"}
       
        if self.__validate_required_fields(email):
            return {"status": "error", "message": "O campo com email do usuário precisa ser preenchido!"}
        
        if self.__validate_required_fields(password):
            return {"status": "error", "message": "O campo com senha do usuário precisa ser preenchido!"}
        
        if self.__validate_required_fields(admin):
            admin = "False"

        if self.__validate_passwords(password, confirm_password):
            return {"status": "error", "message": "As senhas precisam ser iguais!"}
        
        if self.__validate_string_limit(name, 100):
            return {"status": "error", "message": "O nome do usuário precisa ter menos de 100 caracteres!"}
        
        if self.__validate_string_limit(email, 100):
            return {"status": "error", "message": "O email do usuário precisa ter menos de 100 caracteres!"}
        
        if self.__validate_string_limit(password, 20):
            return {"status": "error", "message": "A senha do usuário precisa ter menos de 20 caracteres!"}
        
        if self.__validate_string_minimum(name, 5):
            return {"status": "error", "message": "O nome do usuário precisa ter mais de 5 caracteres!"}
        
        if self.__validate_string_minimum(password, 5):
            return {"status": "error", "message": "A senha do usuário precisa ter mais de 5 caracteres!"}
        


        
        name = name.strip()
        email = email.strip()
        password = password.strip()
        if admin == "True":
            admin = True
        else:
            admin = False
        
        repository = UsersRepository(ConnectionMysqlDB())
        request = repository.select_by_email(email=email)

        if request:
            return {"status": "error", "message": "Email j cadastrado!"}
        
        if request is None:
            return {"status": "error", "message": "Erro ao tentar verificar se email já está cadastrado!"}
        
        request = repository.insert(name=name, email=email, password=password, admin=admin)

        if not request:
            return {"status": "error", "message": "Erro ao tentar registrar usuário no banco de dados!"}
        
        return {"status": "success", "message": "Usuário registrado com sucesso!"}

        

    def __validate_required_fields(self, data: str) -> bool:
        return not data or data.strip() == ""


    def __validate_string_to_float_conversion(self, data: str) -> bool:
        try:
            float(data)
            return False
        
        except:
            return True
        
    def __validate_string_to_integer_conversion(self, data: str) -> bool:
        try:
            int(data)
            return False
        
        except:
            return True


    def __validate_string_limit(self, data:str, limit:int) -> bool:
       return len(data) > limit
    
    def __validate_string_minimum(self, data:str, minimum:int) -> bool:
        return len(data) < minimum
    
    def __validate_passwords(self, password: str, confirm_password: str) -> bool:
        return password != confirm_password
        
