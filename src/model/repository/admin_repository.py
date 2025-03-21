from src.model import ConnectionDataBase
from src.model import Admin


class AdminRepository:

    @staticmethod
    def insert(name:str, email:str, password:str, level=1) -> None:
        with ConnectionDataBase() as connection:
            new_admin = Admin(admin_name=name, admin_email=email, admin_password=password, admin_level=level)
            connection.session.add(new_admin)
            connection.session.commit()

    @staticmethod
    def select() -> list:
        with ConnectionDataBase() as connection:
            query = connection.session.query(Admin).all()
            return query
        
    @staticmethod
    def select_one(id:int) -> object[Admin]:
        with ConnectionDataBase() as connection:
            query = connection.session.query(Admin).filter(Admin.admin_id == id).first()
            return query
        
    @staticmethod
    def update(id:int, name:str = None, email:str = None, password: str = None, level:int = None) -> None:
        parameters = {"admin_name": name, "admin_email": email, "admin_password": password, "admin_level": level}

        for key, value in parameters.items():
            if value:
                parameters = {key:value}

        with ConnectionDataBase() as connection:
            connection.session.query(Admin).filter(Admin.admin_id == id).update(parameters)
            connection.session.commit()

    @staticmethod
    def delete(id:int) -> None:
        with ConnectionDataBase() as connection:
            query = connection.session.query(Admin).filter(Admin.admin_id == id).first()

            if query:
                connection.session.query(Admin).filter(Admin.admin_id == id).delete()
                connection.session.commit()
