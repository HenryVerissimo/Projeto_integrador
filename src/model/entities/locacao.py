from sqlalchemy import Column, Integer, ForeignKey, DateTime, func, Date
from src.model import Base

class Locacao(Base):
    __tablename__ = "locacao"

    id = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey("jogos.id"))
    id_jogo = Column(Integer, ForeignKey("usuarios.id"))
    data_locacao = Column(DateTime, default=func.current_timestamp())
    data_devolucao = Column(Date)

    def __repr__(self):
        return f"locacao(id={self.id}, id_usuario={self.id_usuario}, id_jogo={self.id_jogo}, data_locacao={self.data_locacao}, data_devolucao={self.data_devolucao})"
