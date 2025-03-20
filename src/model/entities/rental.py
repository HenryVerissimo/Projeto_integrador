from sqlalchemy import Column, Integer, ForeignKey, DateTime, func, Date
from src.model import Base

class Rental(Base):
    __tablename__ = "Rental"

    rental_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("jogos.id"))
    game_id = Column(Integer, ForeignKey("usuarios.id"))
    rental_data = Column(DateTime, default=func.current_timestamp())
    return_data = Column(Date)

    def __repr__(self):
        return f"Rental(id={self.rental_id}, id_user={self.user_id}, id_game={self.game_id}, rental_data={self.rental_data}, return_data={self.return_data})"
