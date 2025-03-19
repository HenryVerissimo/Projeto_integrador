from sqlalchemy import Column, Integer, String, Boolean
from src.model import Base

class Usuarios(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    senha = Column(String(20), nullable=False)
    status = Column(Boolean, default=True)

    def __repr__(self):
        return f"usuarios(id={self.id}, nome={self.nome}, email={self.email}, senha={self.senha}, status={self.status})"
