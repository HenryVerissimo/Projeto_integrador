from src.WEB.model import GameRental
from src.WEB.model.config import ConnectionInterfaceDB
from datetime import datetime


class GameRentalRepository:
    def __init__(self, connection: ConnectionInterfaceDB) -> bool:
        self.__connection_db = connection

    def insert(self, user_id:int, game_id:int, date_return: datetime, date_rental: datetime) -> bool:      
            with self.__connection_db as connection:
                try:
                    new_game_rental = GameRental(user_id=user_id, game_id=game_id, game_rental_date=date_rental, game_return_date= date_return)
                    connection.session.add(new_game_rental)
                    connection.session.commit()
                    return True
                
                except Exception as error:
                    print(error)
                    connection.session.rollback()
                    return None

            
    def select(self) -> list:
            with self.__connection_db as connection:
                try:
                    response = connection.session.query(GameRental).all()

                    if not response:
                        return False
                    
                    return response
            
                except Exception as error:
                    return None
        

    def select_by_id(self, id:int) -> GameRental:
            with self.__connection_db as connection:
                try:
                    response = connection.session.query(GameRental).filter(GameRental.game_rental_id == id).first()

                    if not response:
                        return False
                    
                    return response
            
                except Exception as error:
                    return None
        

    def select_by_user_id(self, id:int) -> list:      
            with self.__connection_db as connection:
                try:
                    response = connection.session.query(GameRental).filter(GameRental.user_id == id).all()

                    if not response:
                        return False
                    
                    return response
            
                except Exception as error:
                    return None
        

    def select_by_game_id(self, id:int) -> list:
            with self.__connection_db as connection:
                try:
                    response = connection.session.query(GameRental).filter(GameRental.game_id == id).all()

                    if not response:
                        return False
                    
                    return response
            
                except Exception as error:
                    return None
                

    def select_by_rental_date(self, date: str) -> list:
            with self.__connection_db as connection:
                try:
                    response = connection.session.query(GameRental).filter(GameRental.game_rental_date == date).all()

                    if not response:
                        return False
                    
                    return response
            
                except Exception as error:
                    return None
        

    def select_by_return_date(self, date:str) -> list:
            with self.__connection_db as connection:
                try:
                    response = connection.session.query(GameRental).filter(GameRental.game_return_date == date).first()

                    if not response:
                        return False
                    
                    return response
            
                except Exception as error:
                    return None
 

    def update(self, filter: dict, user_id=None, game_id=None, game_rental_date=None, game_return_date=None) -> bool:
        parameters = {"user_id": user_id, "game_id": game_id, "game_rental_date": game_rental_date, "game_return_date": game_return_date}
        parameters_update = {}

        for key, value in parameters.items():
            if value != None:
                parameters_update[f"{key}"] = value

        with self.__connection_db as connection:
            try:
                if filter["column"] == "game_rental_id":
                    connection.session.query(GameRental).filter(GameRental.game_rental_id == filter["value"]).update(parameters_update)

                elif filter["column"] == "user_id":
                    connection.session.query(GameRental).filter(GameRental.user_id == filter["value"]).update(parameters_update)

                elif filter["column"] == "game_id":
                    connection.session.query(GameRental).filter(GameRental.game_id == filter["value"]).update(parameters_update)

                elif filter["column"] == "game_rental_date":
                    connection.session.query(GameRental).filter(GameRental.game_rental_date == filter["value"]).update(parameters_update)

                elif filter["column"] == "game_return_date":
                    connection.session.query(GameRental).filter(GameRental.game_return_date == filter["value"]).update(parameters_update)

                connection.session.commit()
                return True

            except Exception as error:
                connection.session.rollback()
                return None
            
    
    def delete(self, id:int) -> bool:
        with self.__connection_db as connection:
            try:
                response = connection.session.query(GameRental).filter(GameRental.game_rental_id == id).first()

                if not response:
                    return False
                
                connection.session.delete(response)
                connection.session.commit()
                return True

            except Exception as error:
                connection.session.rollback()
                return None

