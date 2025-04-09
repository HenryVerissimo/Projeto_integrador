from src.WEB.model import ConnectionInterfaceDB
from src.WEB.model import Games

class GamesRepository:
    def __init__(self, connection:ConnectionInterfaceDB) -> None:
        self.__connection_db = connection
    
    def insert(self, name:str, quantity:int, price:float, genre:str, description:str) -> bool:
        with self.__connection_db as connection:
            try:
                new_game = Games(game_name=name, game_quantity=quantity, game_price=price, game_genre=genre, game_description=description)
                connection.session.add(new_game)
                connection.session.commit()
                return True
            
            except Exception as e:
                connection.session.rollback()
                return None

    
    def select(self) -> list:
        try:
            with self.__connection_db as connection:
            
                response = connection.session.query(Games).all()

                if not response:
                    return False
                
                return response
            
        except Exception as e:
            print(e)
            return None
        
    
    def select_by_id(self, id:int) -> Games:
        with self.__connection_db as connection:
            try:
                response = connection.session.query(Games).filter(Games.game_id == id).first()

                if not response:
                    return False
                
                return response
            
            except Exception as error:
                return None
            
    
    def select_by_name(self, name:str) -> list:
        with self.__connection_db as connection:
            try:
                response = connection.session.query(Games).filter(Games.game_name == name).all()

                if not response:
                    return False
                
                return response
            
            except Exception as error:
                return None
            
    def select_by_price(self, price:float) -> list:
        with self.__connection_db as connection:
            try:
                response = connection.session.query(Games).filter(Games.game_price == price).all()

                if not response:
                    return False
                
                return response
            
            except Exception as error:
                return None
            

    def select_by_quantity(self, quantity:int) -> Games:
        with self.__connection_db as connection:
            try:
                response = connection.session.query(Games).filter(Games.game_quantity == quantity).all()

                if not response:
                    return False
                
                return response
            
            except Exception as error:
                return None
            

    def select_by_genre(self, genre:str) -> Games:
        with self.__connection_db as connection:
            try:
                response = connection.session.query(Games).filter(Games.game_genre == genre).all()

                if not response:
                    return False
                
                return response
            
            except Exception as error:
                return None
    
    def update(self, filter: dict, name:str = None, quantity:int = None, price:float = None, genre:str = None, description:str = None) -> bool:
        parameters = {"game_name": name, "game_quantity": quantity, "game_price": price, "game_genre": genre, "game_description": description}
        parameters_update = {}

        for key, value in parameters.items():
            if value != None:
                parameters_update[f"{key}"] = value

        with self.__connection_db as connection:
            try:
                if filter["column"] == "game_id":
                    connection.session.query(Games).filter(Games.game_id == filter["value"]).update(parameters_update)

                elif filter["column"] == "game_name":
                    connection.session.query(Games).filter(Games.game_name == filter["value"]).update(parameters_update)

                elif filter["column"] == "game_quantity":
                    connection.session.query(Games).filter(Games.game_quantity == filter["value"]).update(parameters_update)

                elif filter["column"] == "game_price":
                    connection.session.query(Games).filter(Games.game_price == filter["value"]).update(parameters_update)

                elif filter["column"] == "game_genre":
                    connection.session.query(Games).filter(Games.game_genre == filter["value"]).update(parameters_update)
                
                elif filter["column"] == "game_description":
                    connection.session.query(Games).filter(Games.game_description == filter["value"]).update(parameters_update)

                connection.session.commit()
                return True

            except Exception as error:
                connection.session.rollback()
                return None
        

    def delete(self, id:int) -> bool:
        with self.__connection_db as connection:
            try:
                response = connection.session.query(Games).filter(Games.game_id == id).first()

                if not response:
                    return False
                
                connection.session.query(Games).filter(Games.game_id == id).delete()
                connection.session.commit()
                return True
            
            except Exception as error:
                connection.session.rollback()
                return None
