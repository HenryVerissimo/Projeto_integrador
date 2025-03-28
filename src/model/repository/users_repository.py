from src.model import ConnectionInterfaceDB
from src.model import Users
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound


class UsersRepository:
    def __init__(self, connection: ConnectionInterfaceDB) -> None:
        self.__connection_db = connection


    def insert(self, name:str, email:str, password:str, admin:bool = False) -> bool:
        with self.__connection_db as connection:
            try:
                new_user = Users(user_name=name, user_email=email, user_password=password, user_admin=admin)
                connection.session.add(new_user)
                connection.session.commit()
                return new_user
            
            except Exception as error:
                connection.session.rollback()
                return None


    def select(self) -> list:
        try:
            with self.__connection_db as connection:
                query = connection.session.query(Users).all()
                return query
        
        except ValueError as error:
            return None
            

    def select_one(self,id:int) -> Users:
        try:
            with self.__connection_db as connection:
                query = connection.session.query(Users).filter(Users.user_id == id).first()
                return query
            
        except Exception as error:
            return None
     

    def update(self, id:int, name:str = None, email:str = None, password:int = None, admin:bool = None) -> bool | None:
        parameters = {"user_name": name, "user_email": email, "user_password": password, "user_admin": admin}

        for key, value in parameters.items():
            if value:
                parameters = {key, value}
        
        try:
            with self.__connection_db as connection:
                user = connection.session.query(Users).filter(Users.user_id == id).first()

                if not user:
                    return False
                
                connection.session.query(Users).filter(Users.user_id == id).update(parameters)
                connection.session.commit()
                return True

        except Exception as error:
            connection.session.rollback()
            raise None


    def delete(self, id:int) -> bool:
        try:
            with self.__connection_db as connection:
                user = connection.session.query(Users).filter(Users.user_id == id).first()

                if not user:
                    return False

                connection.session.query(Users).filter(Users.user_id == id).delete()
                connection.session.commit()
                return True

        except Exception as error:
            connection.session.rollback()
            raise None
