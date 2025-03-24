from src.model import ConnectionInterfaceDB
from src.model import Users
from sqlalchemy.exc import DataError


class UsersRepository:
    def __init__(self, connection: ConnectionInterfaceDB) -> None:
        self.__connection_db = connection()


    def insert(self, name:str, email:str, password:str, admin:bool = False, admin_level: int = 0) -> None:
        with self.__connection_db as connection:
            try:
                new_user = Users(user_name=name, user_email=email, user_password=password, user_admin=admin, user_admin_level= admin_level)
                connection.session.add(new_user)
                connection.session.commit()
                response = {
                    "status" : "success",
                    "message" : "Registro criado com sucesso."
                }
                return response

            except Exception as error:
                connection.session.rollback()
                response = {
                    "status" : "error",
                    "message" : f"Erro ao tentar inserir registro no banco: {error}"
                }
                return response


    def select(self) -> list:
        try:
            with self.__connection_db as connection:
                query = connection.session.query(Users).all()

                if query:
                    response = {
                        "status" : "success",
                        "message" : "Registro(s) selecionado(s) com sucesso.",
                        "data": query
                    }
                    return response
                
                response = {
                    "status" : "error",
                    "message" : "Nenhum registro foi encontrado!",
                    "data": query
                }
                return response
        
        except ValueError as error:
            response = {
                "status" : "error",
                "message" : f"Erro ao tentar procurar registros no banco: {error}"
            }
            return response
            

    def select_one(self,id:int) -> object[Users]:
        try:
            with self.__connection_db as connection:
                query = connection.session.query(Users).filter(Users.user_id == id).first()

                if query:
                    response = {
                        "status" : "success",
                        "message" : "Registro foi selecionado com sucesso.",
                        "data": query
                    }
                    return response
                
                response = {
                    "status" : error,
                    "message" : "Nunhum registro foi encontrado."
                }
                return response
            
        except Exception as error:
            response = {
                "status" : "error",
                "message" : f"Erro ao tentar procurar registro no banco: {error}"
            }
            return response
     

    def update(self, id:int, name:str = None, email:str = None, password:int = None, admin:bool = None, admin_level:int = 0) -> None:
        parameters = {"user_name": name, "user_email": email, "user_password": password, "user_admin": admin, "user_admin_level": admin_level}

        for key, value in parameters.items():
            if value:
                parameters = {key, value}
        
        try:
            with self.__connection_db as connection:
                connection.session.query(Users).filter(Users.user_id == id).update(parameters)
                connection.session.commit()
                response = {
                    "status" : "success",
                    "message": "Registro atualizado com sucesso."
                }
                return response

        except Exception as error:
            connection.session.rollback()
            response = {
                "status" : "error",
                "message" : "Erro ao tentar atualizar registro no banco"
            }
            return response


    def delete(self, id:int) -> None:
        try:
            with self.__connection_db as connection:
                query = connection.session.query(Users).filter(Users.user_id == id).first()

                if query:
                    connection.session.query(Users).filter(Users.user_id == id).delete()
                    connection.session.commit()
                    response = {
                        "status" : "success",
                        "message": "Registro deletado com sucesso."
                    }
                    return response
                
                response = {
                    "status" : "error",
                    "message": "Nenhum registro foi encontrado."
                }
                return response

        except Exception as error:
            connection.session.rollback()
            response = {
                "status": "error",
                "message": f"Erro ao tentar deletar registro no banco: {error}"
            }
            return response
