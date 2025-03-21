from src.model import ConnectionDataBase
from src.model import Games

class GamesRepository:
    
    @staticmethod
    def insert(name:str, quantity:int, price:float, genre:str, description:str) -> None:
        with ConnectionDataBase() as connection:
            new_game = Games(game_name=name, game_quantity=quantity, game_price=price, game_genre=genre, game_description=description)
            connection.session.add(new_game)
            connection.session.commit()

    @staticmethod
    def select() -> list:
        with ConnectionDataBase() as connection:
            query = connection.session.query(Games).all()
            return query
        
    @staticmethod
    def select_one(id:int) -> object[Games]:
        with ConnectionDataBase() as connection:
            query = connection.session.query(Games).filter(Games.game_id == id).first()
            return query

    @staticmethod
    def update(id: int, name:str = None, quantity:int = None, price:float = None, genre:str = None, description:str = None) -> None:
        parameters = {"game_name": name, "game_quantity": quantity, "game_price": price, "game_description": description}

        for key, value in parameters.items():
            if value:
                parameters = {key: value}

        with ConnectionDataBase() as connection:
            connection.session.query(Games).filter(Games.game_id == id).update(parameters)
            connection.session.commit()    
        
    @staticmethod
    def delete(id:int) -> None:
        with ConnectionDataBase() as connection:
            query = connection.session.query(Games).filter(Games.game_id == id).first()
            if query:
                connection.session.query(Games).filter(Games.game_id == id).delete()
                connection.session.commit()
