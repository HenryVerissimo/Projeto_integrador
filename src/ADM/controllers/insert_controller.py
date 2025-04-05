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
            return {"status": "error", "message": "Erro ao tentar inserir jogo no banco de dados!"}
        
        return {"status": "success", "message": "Jogo inserido com sucesso!"}
        
    
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
        
