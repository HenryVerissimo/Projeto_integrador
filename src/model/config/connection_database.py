from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from abc import ABC, abstractmethod


class ConnectionInterfaceDB(ABC):
 
    @abstractmethod
    def _create_engine(self):
        pass

    @abstractmethod
    def get_engine(self):
        pass

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class ConnectionMysqlDB(ConnectionInterfaceDB):
    def __init__(self):
        self.__engine_string = "mysql+pymysql://User:Password123@192.168.120.154:3306/GameRental" #Trocar para o ip do servidor local no dia da apresentação
        self.__engine = self._create_engine()
        self.session = None

    def _create_engine(self):
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
