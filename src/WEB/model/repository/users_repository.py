from src.WEB.model import ConnectionInterfaceDB
from src.WEB.model import Users


class UsersRepository:
    def __init__(self, connection: ConnectionInterfaceDB) -> None:
        self.__connection_db = connection


    def insert(self, name:str, email:str, password:str, admin:bool = False, status:bool = True) -> bool:
        with self.__connection_db as connection:
            try:
                new_user = Users(user_name=name, user_email=email, user_password=password, user_admin=admin, user_status=status)
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

            
    def select_by_id(self,id:int) -> Users:
        try:
            with self.__connection_db as connection:
                response = connection.session.query(Users).filter(Users.user_id == id).first()

                if not response:
                    return False
                
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
        
    def select_by_status(self, status: bool) -> Users:

        try:
            with self.__connection_db as connection:
                response = connection.session.query(Users).filter(Users.user_status == status).all()

                if not response:
                    return False
                
                return response
            
        except Exception as error:
            return None
        

    def select_by_admin(self, admin: bool) -> Users:
        try:
            with self.__connection_db as connection:
                response = connection.session.query(Users).filter(Users.user_admin == admin).all()

                if not response:
                    return False
                
                return response
        
        except Exception as error:
            return None

    def update(self, filter: dict, name:str = None, email:str = None, password:int = None, admin:bool = None, status:bool = None) -> bool | None:
        parameters = {"user_name": name, "user_email": email, "user_password": password, "user_admin": admin, "user_status": status}
        parameters_update = {}

        for key, value in parameters.items():
            if value != None:
                parameters_update[f"{key}"] = value
        
        try:
            with self.__connection_db as connection:
                
                if filter["column"] == "user_id":
                    connection.session.query(Users).filter(Users.user_id == filter["value"]).update(parameters_update)

                elif filter["column"] == "user_name":
                    connection.session.query(Users).filter(Users.user_name == filter["value"]).update(parameters_update)

                elif filter["column"] == "user_email":
                    connection.session.query(Users).filter(Users.user_email == filter["value"]).update(parameters_update)

                elif filter["column"] == "user_password":
                    connection.session.query(Users).filter(Users.user_password == filter["value"]).update(parameters_update)

                elif filter["column"] == "user_admin":
                    connection.session.query(Users).filter(Users.user_admin == filter["value"]).update(parameters_update)

                elif filter["column"] == "user_status":
                    connection.session.query(Users).filter(Users.user_status == filter["value"]).update(parameters_update)

                connection.session.commit()
                return True

        except Exception as error:
            connection.session.rollback()
            return False


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
