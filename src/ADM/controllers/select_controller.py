from src.model.repository import UsersRepository, GameRentalRepository, GamesRepository
from abc import ABC, abstractmethod
from src.model.config import ConnectionMysqlDB
from src.model.entities import Users, Games, GameRental
from datetime import datetime


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

        if column not in ["Todas"] and value in ["", None]:
            return {"status": "error", "response": "", "message": "Forneça um parâmetro para filtragem!"}
        
        if value == "False":
            value = False

        elif value == "True":
            value = True   

        if column == "ID":
            request = repository.select_by_id(id=int(value))

        elif column == "Nome":
            request = repository.select_by_name(name=value)

        elif column == "Email":
            request = repository.select_by_email(email=value)

        elif column == "Admin":

            request = repository.select_by_admin(admin=value)

        elif column == "Status":

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
                response.append({"id": f"{game.game_id}", "name": f"{game.game_name}", "price": f"{game.game_price}", "quantity": f"{game.game_quantity}", "genre": f"{game.game_genre}"})

        elif isinstance(request, Games):
            response.append({"id": f"{request.game_id}", "name": f"{request.game_name}", "price": f"{request.game_price}", "quantity": f"{request.game_quantity}", "genre": f"{request.game_genre}"})
        
        return {"status": "success", "response": response, "message": "Jogos encontrados com sucesso!"}
    

    @abstractmethod
    def select_games_rental_by_filter(column: str, value: str) -> dict:
        repository = GameRentalRepository(ConnectionMysqlDB())
        response = []

        if column not in ["Todas"] and value in ["", None]:
            return {"status": "error", "response": "", "message": "Forneça um parâmetro para filtragem!"}  

        if column == "ID":
            request = repository.select_by_id(id=int(value))

        elif column == "ID do usuário":
            request = repository.select_by_user_id(id=value)

        elif column == "ID do jogo":
            request = repository.select_by_game_id(id=value)

        elif column == "Data de aluguel":

            if "/" in value:
                value = value.replace("/", "-")

            count_char = 0
            for number in value:
                if number == "-":
                    break

                count_char += 1

            if count_char == 2:
                date_split = value.split("-")
                value = f"{date_split[2]}-{date_split[1]}-{date_split[0]}"

            value = datetime.strptime(value, "%Y-%m-%d").date()

            request = repository.select_by_rental_date(date=value)

        elif column == "Data de devolução":

            if "/" in value:
                value = value.replace("/", "-")

            count_char = 0
            for number in value:
                if number == "-":
                    break

                count_char += 1

            if count_char == 2:
                date_split = value.split("-")
                value = f"{date_split[2]}-{date_split[1]}-{date_split[0]}"
                

            value = datetime.strptime(value, "%Y-%m-%d").date()

            request = repository.select_by_return_date(date=value)

        if request is False:
            return {"status": "error", "response": "", "message": "Nenhum aluguel encontrado!"}
        
        elif request is None:
            return {"status": "error", "response": "", "message": "Erro ao tentar encontrar aluguéis no banco de dados!"}
        
        if isinstance(request, list):

            for rental in request:
                response.append({"rental_id": f"{rental.game_rental_id}", "user_id": f"{rental.user_id}", "game_id": f"{rental.game_id}", "rental_date": f"{rental.game_rental_date}", "return_date": f"{rental.game_return_date}"})

        elif isinstance(request, GameRental):
            response.append({"rental_id": f"{request.game_rental_id}", "user_id": f"{request.user_id}", "game_id": f"{request.game_id}", "rental_date": f"{request.game_rental_date}", "return_date": f"{request.game_return_date}"})
        
        return {"status": "success", "response": response, "message": "Aluguéis encontrados com sucesso!"}