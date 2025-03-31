from src.model import GameRental, Games


class GameRentalRepository:
    def __init__(self, connection) -> bool:
        self.__connection_db = connection

    def insert(self, user_id:int, game_id:int, date_return: str) -> bool:
        try:
            with self.__connection_db as connection:
                new_game_rental = GameRental(user_id=user_id, game_id=game_id, game_return_date=date_return)
                connection.session.add(new_game_rental)
                connection.session.commit()
                return True
            
        except Exception as error:
            connection.session.rollback()
            return False

    def select(self) -> list:
        try:
            with self.__connection_db as connection:
                query = connection.session.query(GameRental).all()

                if not query:
                    return False
                
                return query
            
        except Exception as error:
            return None
 

    def update(self, id: int, user_id=None, game_id=None, game_rental_date=None, game_return_date=None) -> bool:
        parameters = {"user_id": user_id, "game_id": game_id, "game_rental_date": game_rental_date, "game_return_date": game_return_date}

        for key, value in parameters.items():
            if value:
                parameters = {key: value}

        with self.__connection_db as connection:
            try:
                connection.session.query(Games).filter(Games.game_id == id).update(parameters)
                connection.session.commit()
                return True

            except Exception as error:
                connection.session.rollback()
                return None
            
    
    def delete(self, id:int) -> bool:
        with self.__connection_db as connection:
            try:
                query = connection.session.query(Games).filter(Games.game_id == id).first()

                if not query:
                    return False
                
                connection.session.delete(query)
                connection.session.commit()
                return True

            except Exception as error:
                connection.session.rollback()
                return None

