from sqlalchemy.orm.exc import NoResultFound
from src.model import ConnectionInterfaceDB
from src.model import Games

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
            
            except Exception as error:
                connection.session.rollback()
                raise f"Erro ao tentar inserir registro ao banco: {error}"

    
    def select(self) -> list:
        with self.__connection_db as connection:
            try:
                query = connection.session.query(Games).all()

                if not query:
                    raise NoResultFound("Nenhum registro foi encontrado.")
                
                return query
            
            except Exception as error:
                raise f"Erro ao tentar procurar registros no banco: {error}"
        
    
    def select_one(self, id:int) -> Games:
        with self.__connection_db as connection:
            try:
                query = connection.session.query(Games).filter(Games.game_id == id).first()

                if not query:
                    raise NoResultFound("Nenhum registro foi encontrado com esse id")
                
                return query
            
            except Exception as error:
                raise f"Erro ao tentar procurar o registro no banco: {error}" 

    
    def update(self, id: int, name:str = None, quantity:int = None, price:float = None, genre:str = None, description:str = None) -> bool:
        parameters = {"game_name": name, "game_quantity": quantity, "game_price": price, "game_description": description}

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
                raise f"Erro ao tentar atualizar registro no banco: {error}"
        

    def delete(self, id:int) -> bool:
        with self.__connection_db as connection:
            try:
                query = connection.session.query(Games).filter(Games.game_id == id).first()

                if not query:
                    raise NoResultFound("Nenhum registro encontrado com esse id")
                
                connection.session.query(Games).filter(Games.game_id == id).delete()
                connection.session.commit()
                return True
            
            except Exception as error:
                connection.session.rollback()
                raise f"Erro ao tentar deletar registro do banco: {error}"
