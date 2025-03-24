from src.model import ConnectionMysqlDB
from src.model import GameRental
from sqlalchemy.orm.exc import NoResultFound 


class GameRentalRepository:

    def select() -> list:
        try:
            with ConnectionMysqlDB() as connection:
                query = connection.session.query(GameRental).all()

                if not query:
                    raise  NoResultFound("Nenhum registro foi encontrado.")
                
                return query
            
        except Exception as error:
            raise f"Erro ao tentar procurar o registro no banco: {error}"
 

    def insert(date:str) -> None:
        with ConnectionMysqlDB() as connection:
            try:
                new_location = GameRental(game_return_date=date) 
                connection.session.add(new_location)
                connection.session.commit()
                return True
            
            except Exception as error:
                connection.session.rollback()
                raise f"Erro ao tentar inserir registro ao banco: {error}"
