from src.model import ConnectionInterfaceDB
from src.model import Users


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
                response = connection.session.query(Users).all()

                if not response:
                    return False
                
                return response
        
        except ValueError as error:
            return None

            
    def select_one_by_id(self,id:int) -> Users:
        try:
            with self.__connection_db as connection:
                response = connection.session.query(Users).filter(Users.user_id == id).first()
                return response
            
        except Exception as error:
            return None
        
    def select_by_email(self, email:str) -> Users:
        try:
            with self.__connection_db as connection:
                response = connection.session.query(Users).filter(Users.user_email == email).first()
                
                if not response:
                    return False
                
                return response
            
        except Exception as error:
            return None
        
    def select_by_name(self, name: str) -> Users:
        try:
            with self.__connection_db as connetion:
                response = connetion.session.query(Users).filter(Users.user_name == name).all()

                if not response:
                    return False
                
                return response
            
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
                request = connection.session.query(Users).filter(Users.user_id == id).first()

                if not request:
                    return False

                connection.session.delete(request)
                connection.session.commit()
                return True

        except Exception as error:
            connection.session.rollback()
            raise None
