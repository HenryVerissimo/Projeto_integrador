from src.model import ConnectionDataBase
from src.model import Jogos

class JogosRepository:
    
    @staticmethod
    def insert(nome:str, preco:float, genero:str, descricao:str) -> None:
        with ConnectionDataBase() as conection:
            novo_jogo = Jogos(nome, preco, genero, descricao)
            conection.session.add(novo_jogo)
            conection.session.commit()

    @staticmethod
    def select() -> list:
        with ConnectionDataBase() as connection:
            query = connection.session.query(Jogos).all()
            
            return query
    @staticmethod
    def delete(id: int) -> None:
        with ConnectionDataBase() as connection:
            query = connection.session.query(Jogos).filter(Jogos.id == id).first()
            if query is not None:
                connection.session.query(Jogos).filter(Jogos.id == id).delete()
                connection.session.commit()
