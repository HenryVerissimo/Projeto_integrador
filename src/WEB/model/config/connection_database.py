from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from abc import ABC, abstractmethod

from os import getenv
from dotenv import load_dotenv

load_dotenv()
url_db = getenv("URL_DB")


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
        self.__engine_string = f"{url_db}"
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
