from src.model import ConnectionDataBase
from src.model import FilmLocation


class FilmLocationRepository:

    @staticmethod
    def insert(data:str) -> None:
        with ConnectionDataBase() as connection:
            new_location = FilmLocation(filme_location_data=data) 
            connection.session.add(new_location)
            connection.session.commit()