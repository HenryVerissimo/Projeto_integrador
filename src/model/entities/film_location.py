from sqlalchemy import Column, Integer, ForeignKey, DateTime, func, Date
from src.model import Base

class FilmLocation(Base):
    __tablename__ = "film_location"

    filme_location_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("jogos.id"))
    game_id = Column(Integer, ForeignKey("usuarios.id"))
    film_location_data = Column(DateTime, default=func.current_timestamp())
    return_data = Column(Date)

    def __repr__(self):
        return f"film location (id={self.rental_id}, user_id={self.user_id}, game_id={self.game_id}, film_location_data={self.film_location_data}, return_data={self.return_data})"
