from src.model import ConnectionDataBase
from src.model import Users


class UsersRepository:

    @staticmethod
    def insert(name:str, email:str, password:str, admin:bool = False, admin_level: int = 0) -> None:
        with ConnectionDataBase() as connect:
            new_user = Users(user_name=name, user_email=email, user_password=password, user_admin=admin, user_admin_level= admin_level)
            connect.session.add(new_user)
            connect.session.commit()

    @staticmethod
    def select() -> list:
        with ConnectionDataBase() as connect:
            query = connect.session.query(Users).all()
            return query

    @staticmethod
    def select_one(id:int) -> object[Users]:
        with ConnectionDataBase() as connection:
            query = connection.session.query(Users).filter(Users.user_id == id).first()
            return query
    
    @staticmethod   
    def update(id:int, name:str = None, email:str = None, password:int = None, admin:bool = None, admin_level:int = 0) -> None:
        parameters = {"user_name": name, "user_email": email, "user_password": password, "user_admin": admin, "user_admin_level": admin_level}

        for key, value in parameters.items():
            if value:
                parameters = {key, value}

        with ConnectionDataBase() as connect:
            connect.session.query(Users).filter(Users.user_id == id).update(parameters)
            connect.session.commit()

    @staticmethod
    def delete(id:int) -> None:
        with ConnectionDataBase() as connect:
            query = connect.session.query(Users).filter(Users.user_id == id).first()

            if query:
                connect.session.query(Users).filter(Users.user_id == id).delete()
