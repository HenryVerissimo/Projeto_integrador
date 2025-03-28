from src.model import ConnectionMysqlDB
from src.model import GameRental, Games
from sqlalchemy.orm.exc import NoResultFound


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
            return f"Erro ao tentar inserir registro ao banco"

    def select(self) -> list:
        try:
            with self.__connection_db as connection:
                query = connection.session.query(GameRental).all()

                if not query:
                    raise  NoResultFound("Nenhum registro foi encontrado.")
                
                return query
            
        except Exception as error:
            return f"Erro ao tentar procurar o registro no banco"
 

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
                return f"Erro ao tentar atualizar registro no banco"
            
    
    def delete(self, id:int) -> bool:
        with self.__connection_db as connection:
            try:
                query = connection.session.query(Games).filter(Games.game_id == id).first()

                if not query:
                    raise NoResultFound("Não foi encontrado nenhum registro com esse id")
                
                connection.session.query(Games).filter(Games.game_id == id).delete()
                connection.session.commit()
                return True

            except Exception as error:
                connection.session.rollback()
                return f"Erro ao tentar deletar registro no banco"

