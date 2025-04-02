from src.model.repository import UsersRepository, GameRentalRepository, GamesRepository
from abc import ABC, abstractmethod
from src.model.config import ConnectionMysqlDB
from src.model.entities import Users, Games, GameRental


class SelectController(ABC):

    @abstractmethod
    def select_all_users() -> dict:

            request = UsersRepository(ConnectionMysqlDB()).select()
            response = []

            if request is False:
                return {"status": "error", "response": response, "message": "Nenhum usuário encontrado!"}
            
            elif request is None:
                return {"status": "error", "response": response, "message": "Erro ao tentar encontrar usuários no banco de dados!"}
            
            for user in request:
                response.append({"id": f"{user.user_id}", "name": f"{user.user_name}", "email": f"{user.user_email}", "admin": f"{user.user_admin}", "status": f"{user.user_status}"})

            return {"status": "success", "response": response, "message": "Usuários encontrados com sucesso!"}
    

    @abstractmethod
    def select_all_games() -> dict:

        request = GamesRepository(ConnectionMysqlDB()).select()
        response = []

        if request is False:
            return {"status": "error", "response": response, "message": "Nenhum jogo encontrado!"}
        
        elif request is None:
            return {"status": "error", "response": response, "message": "Erro ao tentar encontrar jogos no banco de dados!"}
        
        for game in request:
            response.append({"id": f"{game.game_id}", "name": f"{game.game_name}", "price": f"{game.game_price}", "quantity": f"{game.game_quantity}", "genre": f"{game.game_genre}", "description": f"{game.game_description}"})
        
        return {"status": "success", "response": response, "message": "Jogos encontrados com sucesso!"}
    

    @abstractmethod
    def select_all_games_rental() -> dict:

        request = GameRentalRepository(ConnectionMysqlDB()).select()
        response = []

        if request is False:
            return {"status": "error", "response": "", "message": "Nenhum jogo alugado encontrado!"}
        
        elif request is None:
            return {"status": "error", "response": "", "message": "Erro ao tentar encontrar jogos no banco de dados!"}
        
        for rental in request:
            response.append({"rental_id": f"{rental.game_rental_id}", "user_id": f"{rental.user_id}", "game_id": f"{rental.game_id}", "rental_date": f"{rental.game_rental_date}", "return_date": f"{rental.game_return_date}"})

        return {"status": "success", "response": response, "message": "Jogos encontrados com sucesso!"}
    

    @abstractmethod
    def select_users_by_filter(column: str, value: str) -> dict:

        repository = UsersRepository(ConnectionMysqlDB())
        response = []

        if column == "ID":
            request = repository.select_by_id(id=int(value))

        elif column == "Nome":
            request = repository.select_by_name(name=value)

        elif column == "Email":
            request = repository.select_by_email(email=value)

        elif column == "Admin":

            if value == "True":
                value = True
            
            elif value == "False":
                value = False

            request = repository.select_by_admin(admin=value)

        elif column == "Status":

            if value == "True":
                value = True
            
            elif value == "False":
                value = False

            request = repository.select_by_status(status=value)

        if request is False:
            return {"status": "error", "response": "", "message": "Nenhum usuário encontrado!"}
        
        elif request is None:
            return {"status": "error", "response": "", "message": "Erro ao tentar encontrar usuários no banco de dados!"}
        
        if isinstance(request, list):

            for user in request:
                response.append({"id": f"{user.user_id}", "name": f"{user.user_name}", "email": f"{user.user_email}", "admin": f"{user.user_admin}", "status": f"{user.user_status}"})

        elif isinstance(request, Users):
            response.append({"id": f"{request.user_id}", "name": f"{request.user_name}", "email": f"{request.user_email}", "admin": f"{request.user_admin}", "status": f"{request.user_status}"})
        
        return {"status": "success", "response": response, "message": "Usuários encontrados com sucesso!"}

        