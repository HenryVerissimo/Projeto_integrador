from sqlalchemy import Column, Integer, String, DECIMAL, Text
from src.model import Base



class Games(Base):
    __tablename__ = "games"

    game_id = Column(Integer, primary_key=True)
    game_name = Column(String(100), nullable=False)
    game_price = Column(DECIMAL(10, 2), nullable=False )
    game_quantity = Column(Integer, default=0)
    game_genre = Column(String(100))
    game_description= Column(Text)
    
    def __repr__(self):
        return f"Games(game_id={self.game_id}, gane_name={self.game_name}, game_price={self.game_price}, game_genre={self.game_genre}, game_description={self.game_description})"
 