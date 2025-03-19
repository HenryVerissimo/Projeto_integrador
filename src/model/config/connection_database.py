from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class ConnectionDataBase:
    def __init__(self):
        self.__engine_string = "mysql+pymql//User:Senha123@localhost/LocacaoJogos" #Trocar para o ip do servidor local no dia da apresentação
        self.__engine = self.__create_engine()
        self.session = None

    def __create_engine(self):
        return create_engine(self.__engine_string)
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        Session = sessionmaker(bind=self.__engine)
        self.session = Session()

        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            self.session.close()
