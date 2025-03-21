from src.model import ConnectionDataBase
from src.model import GameRental


class GameRentalRepository:

    @staticmethod
    def insert(date:str) -> None:
        with ConnectionDataBase() as connection:
            new_location = GameRental(game_return_date=date) 
            connection.session.add(new_location)
            connection.session.commit()