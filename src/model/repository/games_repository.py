from sqlalchemy.orm.exc import NoResultFound
from src.model import ConnectionMysqlDB
from src.model import Games

class GamesRepository:
    
    @staticmethod
    def insert(name:str, quantity:int, price:float, genre:str, description:str) -> None:
        with ConnectionMysqlDB() as connection:
            try:
                new_game = Games(game_name=name, game_quantity=quantity, game_price=price, game_genre=genre, game_description=description)
                connection.session.add(new_game)
                connection.session.commit()
                return True
            
            except Exception as error:
                connection.session.rollback()
                raise f"Erro ao tentar inserir registro ao banco: {error}"

    @staticmethod
    def select() -> list:
        with ConnectionMysqlDB() as connection:
            try:
                query = connection.session.query(Games).all()

                if not query:
                    raise NoResultFound("Nenhum registro foi encontrado.")
                
                return query
            
            except Exception as error:
                raise f"Erro ao tentar procurar registros no banco: {error}"
        
    @staticmethod
    def select_one(id:int) -> object[Games]:
        with ConnectionMysqlDB() as connection:
            try:
                query = connection.session.query(Games).filter(Games.game_id == id).first()

                if not query:
                    raise NoResultFound("Nenhum registro foi encontrado com esse id")
                
                return query
            
            except Exception as error:
                raise f"Erro ao tentar procurar o registro no banco: {error}" 

    @staticmethod
    def update(id: int, name:str = None, quantity:int = None, price:float = None, genre:str = None, description:str = None) -> None:
        parameters = {"game_name": name, "game_quantity": quantity, "game_price": price, "game_description": description}

        for key, value in parameters.items():
            if value:
                parameters = {key: value}

        with ConnectionMysqlDB() as connection:
            connection.session.query(Games).filter(Games.game_id == id).update(parameters)
            connection.session.commit()    
        
    @staticmethod
    def delete(id:int) -> None:
        with ConnectionMysqlDB() as connection:
            query = connection.session.query(Games).filter(Games.game_id == id).first()
            if query:
                connection.session.query(Games).filter(Games.game_id == id).delete()
                connection.session.commit()
