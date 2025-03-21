from src.model import ConnectionDataBase
from src.model import Users


class UsersRepository:

    @staticmethod
    def insert(name:str, email:str, password:str) -> None:
        with ConnectionDataBase() as connect:
            new_user = Users(user_name=name, user_email=email, user_password=password)
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
    def update(id:int, name:str = None, email:str = None, password:int = None) -> None:
        parameters = {"user_name": name, "user_email": email, "user_password": password}

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
