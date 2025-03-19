from sqlalchemy import Column, Integer, String, DECIMAL, Text
from src.model import Base



class Jogos(Base):
    __tablename__ = "jogos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    preco = Column(DECIMAL(10, 2), nullable=False )
    genero = Column(String(100))
    descricao = Column(Text)

    def __repr__(self):
        return f"Jogos(id={self.id}, nome={self.nome}, preco={self.preco}, genero={self.genero}, descricao={self.descricao})"
 