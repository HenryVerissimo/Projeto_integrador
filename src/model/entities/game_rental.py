from sqlalchemy import Column, Integer, ForeignKey, DateTime, func, Date
from src.model import Base

class GameRental(Base):
    __tablename__ = "game_rental"

    game_rental_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("jogos.id"))
    game_id = Column(Integer, ForeignKey("usuarios.id"))
    game_rental_date = Column(DateTime, default=func.current_timestamp())
    game_return_date = Column(Date)

    def __repr__(self):
        return f"game rental (game_rental_id={self.game_rental_id}, user_id={self.user_id}, game_id={self.game_id}, game_rental_date={self.game_rental_date}, game_return_date={self.game_return_date})"
