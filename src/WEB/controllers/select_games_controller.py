from src.WEB.model.repository import GamesRepository
from abc import ABC, abstractmethod
from src.WEB.model.config import ConnectionMysqlDB
from src.WEB.model.entities import Games


class SelectGamesController(ABC):

    @abstractmethod
    def select_all_games() -> dict:

        request = GamesRepository(ConnectionMysqlDB()).select()
        response = []

        if request is False:
            return {"status": "error", "response": response, "message": "Nenhum jogo encontrado!"}
        
        elif request is None:
            return {"status": "error", "response": response, "message": "Erro ao tentar encontrar jogos no banco de dados!"}
        
        for game in request:
            response.append({"id": f"{game.game_id}", "name": f"{game.game_name}", "price": game.game_price, "quantity": game.game_quantity, "genre": f"{game.game_genre}", "description": f"{game.game_description}"})
        
        return {"status": "success", "response": response, "message": "Jogos encontrados com sucesso!"}
    

    @abstractmethod
    def select_games_by_filter(column: str, value: str) -> dict:
        repository = GamesRepository(ConnectionMysqlDB())
        response = []

        if column not in ["Todas"] and value in ["", None]:
            return {"status": "error", "response": "", "message": "Forneça um parâmetro para filtragem!"}  

        if column == "ID":
            request = repository.select_by_id(id=int(value))

        elif column == "Nome":
            request = repository.select_by_name(name=value)

        elif column == "Preço":
            request = repository.select_by_price(price=value)

        elif column == "Quantidade":

            request = repository.select_by_quantity(quantity=value)

        elif column == "Genero":

            request = repository.select_by_genre(genre=value)

        if request is False:
            return {"status": "error", "response": "", "message": "Nenhum Jogo encontrado!"}
        
        elif request is None:
            return {"status": "error", "response": "", "message": "Erro ao tentar encontrar Jogos no banco de dados!"}
        
        if isinstance(request, list):

            for game in request:
                response.append({"id": f"{game.game_id}", "name": f"{game.game_name}", "price": game.game_price, "quantity": game.game_quantity, "genre": f"{game.game_genre}", "description": f"{game.game_description}"})

        elif isinstance(request, Games):
            response.append({"id": f"{request.game_id}", "name": f"{request.game_name}", "price": request.game_price, "quantity": request.game_quantity, "genre": f"{request.game_genre}", "description": f"{request.game_description}"})
        
        return {"status": "success", "response": response, "message": "Jogos encontrados com sucesso!"}
