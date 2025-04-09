from src.WEB.model.config import ConnectionMysqlDB
from src.WEB.model.repository import GameRentalRepository, UsersRepository, GamesRepository
from src.WEB.model.entities import Users, GameRental, Games


class DeleteController:

    def delete_user(self, id: str) -> dict:
        if self.__validate_string_to_integer_conversion(id):
            return {"status": "error", "message": "ID do usuário precisa ser um número inteiro!"}
        
        id = int(id)
        repository = GameRentalRepository(ConnectionMysqlDB())
        request = repository.select_by_user_id(id)

        if request:
            for rental in request:
                rental_id = str(rental.game_rental_id)
                repository.delete(rental_id)

        repository = UsersRepository(ConnectionMysqlDB())
        request = repository.delete(id=id)

        if request is False:
            return {"status": "error", "message": "Nenhum usuário com esse ID foi encontrado!"}
        
        elif request is None:
            return {"status": "error", "message": "Erro ao tentar deletar usuário no banco!"}
        
        return {"status": "success", "message": "Usuário deletado com sucesso!"}
    

    def delete_game(self, id: str) -> dict:
        if self.__validate_string_to_integer_conversion(id):
            return {"status": "error", "message": "ID do jogo precisa ser um número inteiro!"}
        
        id = int(id)
        repository = GameRentalRepository(ConnectionMysqlDB())
        request = repository.select_by_game_id(id)

        if request:
            for rental in request:
                rental_id = rental_id = str(rental.game_rental_id)
                repository.delete(rental_id)

        repository = GamesRepository(ConnectionMysqlDB())
        request = repository.delete(id=id)

        if request is False:
            return {"status": "error", "message": "Nenhum jogo com esse ID foi encontrado!"}
        
        elif request is None:
            return {"status": "error", "message": "Erro ao tentar deletar jogo no banco!"}
        
        return {"status": "success", "message": "Jogo deletado com sucesso!"}
    
    def delete_game_rental(self, id: str) -> dict:

        repository = GameRentalRepository(ConnectionMysqlDB())

        if self.__validate_string_to_integer_conversion(id):
            return {"status": "error", "message": "ID do aluguel precisa ser um número inteiro!"}
        
        id = int(id)
        request = repository.delete(id)

        if request is False:
            return {"status": "error", "message": "Nenhum aluguel com esse ID foi encontrado!"}
        
        elif request is None:
            return {"status": "error", "message": "Erro ao tentar deletar aluguel no banco!"}
        
        return {"status": "success", "message": "Aluguel deletado com sucesso"}


    def __validate_string_to_integer_conversion(self, data: str) -> bool:
        try:
            int(data)
            return False
        
        except:
            return True