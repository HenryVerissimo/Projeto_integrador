from sqlalchemy import Column, Integer, String, DECIMAL, Text
from src.model import Base



class Games(Base):
    __tablename__ = "Games"

    game_id = Column(Integer, primary_key=True)
    game_name = Column(String(100), nullable=False)
    game_price = Column(DECIMAL(10, 2), nullable=False )
    game_genre = Column(String(100))
    game_description= Column(Text)
    
    def __repr__(self):
        return f"Games(id={self.game_id}, name={self.game_name}, price={self.game_price}, genre={self.game_genre}, description={self.game_description})"
 