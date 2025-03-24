from src.model import ConnectionMysqlDB
from src.model import GameRental


class GameRentalRepository:

    def select() -> list:
        try:
            with ConnectionMysqlDB() as connection:
                query = connection.session.query(GameRental).all()

                if query:
                    response = {
                        "status": "success",
                        "message": "Registro(s) selecionado(s) com successo.",
                        "data": query

                    }
                    return response
                
                response = {
                    "status": "error",
                    "message": "Nenhum registro foi encontrado!"
                }
                return response
            
        except Exception as error:
            response = {
                "status": "error",
                "message": f"erro ao tentar procurar registros no banco: {error}"
            }
            return response
 

    def insert(date:str) -> None:
        with ConnectionMysqlDB() as connection:
            try:
                new_location = GameRental(game_return_date=date) 
                connection.session.add(new_location)
                connection.session.commit()
                response = {
                    "status": "success",
                    "message": "Registro criado com sucesso."
                }
                return response
            
            except Exception as error:
                connection.session.rollback()
                response = {
                    "status": "error",
                    "message": f"Erro ao tentar inserir registro no banco: {error}"
                }
                return response