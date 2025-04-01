from src.model.repository import UsersRepository, GameRentalRepository, GamesRepository
from src.model.config import ConnectionMysqlDB
from src.model.entities import Users, Games, GameRental


class SelectController:

    def select_all_users(self) -> dict:

            request = UsersRepository(ConnectionMysqlDB()).select()
            response = []

            if request is False:
                return {"status": "error", "response": response, "message": "Nenhum usuário encontrado!"}
            
            elif request is None:
                return {"status": "error", "response": response, "message": "Erro ao tentar encontrar usuários no banco de dados!"}
            
            for user in request:
                response.append({"id": f"{user.user_id}", "name": f"{user.user_name}", "email": f"{user.user_email}", "admin": f"{user.user_admin}", "status": f"{user.user_status}"})

            return {"status": "success", "response": response, "message": "Usuários encontrados com sucesso!"}
    
    
    def select_all_games(self) -> dict:

        request = GamesRepository(ConnectionMysqlDB()).select()
        response = []

        if request is False:
            return {"status": "error", "response": response, "message": "Nenhum jogo encontrado!"}
        
        elif request is None:
            return {"status": "error", "response": response, "message": "Erro ao tentar encontrar jogos no banco de dados!"}
        
        for game in request:
            response.append({"id": f"{game.game_id}", "name": f"{game.game_name}", "price": f"{game.game_price}", "quantity": f"{game.game_quantity}", "genre": f"{game.game_genre}", "description": f"{game.game_description}"})
        
        return {"status": "success", "response": response, "message": "Jogos encontrados com sucesso!"}
    

    def select_all_games_rental(self) -> dict:

        request = GameRentalRepository(ConnectionMysqlDB()).select()
        response = []

        if request is False:
            return {"status": "error", "response": "", "message": "Nenhum jogo alugado encontrado!"}
        
        elif request is None:
            return {"status": "error", "response": "", "message": "Erro ao tentar encontrar jogos no banco de dados!"}
        
        for rental in request:
            response.append({"rental_id": f"{rental.game_rental_id}", "user_id": f"{rental.user_id}", "game_id": f"{rental.game_id}", "rental_date": f"{rental.game_rental_date}", "return_date": f"{rental.game_return_date}"})

        return {"status": "success", "response": response, "message": "Jogos encontrados com sucesso!"}