from src.WEB.model.repository import UsersRepository, GamesRepository, GameRentalRepository
from src.WEB.model.config import ConnectionMysqlDB
from src.WEB.model.entities import Users, Games, GameRental
from datetime import datetime


class UpdateController:

    def update_user(self, name: str, email: str, password: str, admin: str, status: str, filter_column: str, filter_value: str) -> dict:

        repository = UsersRepository(ConnectionMysqlDB())

        if not filter_value:
            return {"status": "error", "response": "", "message": "Forneça um parâmetro para filtragem!"}
        
        if name is None and email is None and password is None and admin is None and status is None:
            return {"status": "error", "response": "", "message": "Forneça um parâmetro para atualização!"}
        
        if name:
            name = name.strip()
            if self.__validate_string_limit(name, 100):
                return {"status": "error", "response": "", "message": "O nome do usuário precisa ter menos de 100 caracteres!"}

            if self.__validate_string_minimum(name, 5):
                return {"status": "error", "response": "", "message": "O nome do usuário precisa ter mais de 5 caracteres!"}

        if email:
            email = email.strip()
            if self.__validate_email(email):
                return {"status": "error", "response": "", "message": "O formato do email é inválido!"}

            if self.__validate_email_exists(email):
                return {"status": "error", "response": "", "message": "Email já cadastrado!"}
            
        if password:
            password = password.strip()
            if self.__validate_string_minimum(password, 5):
                return {"status": "error", "response": "", "message": "A senha precisa ter mais de 5 caracteres!"}

            if self.__validate_string_limit(password, 20):
                return {"status": "error", "response": "", "message": "A senha precisa ter menos de 20 caracteres!"}
        
        if admin:
            if admin == "True":
                admin = 1
            elif admin == "False":
                admin = 0

        if status:
            if status == "True":
                status = 1
            elif status == "False":
                status = 0
        
        if filter_column == "ID":
            request = repository.select_by_id(id=int(filter_value))

        elif filter_column == "Nome":
            request = repository.select_by_name(name=filter_value)

        elif filter_column == "Email":
            request = repository.select_by_email(email=filter_value)

        elif filter_column == "Admin":
            if filter_value == "True":
                filter_value = 1
            
            elif filter_value == "False":
                filter_value = 0

            request = repository.select_by_admin(admin=filter_value)

        elif filter_column == "Status":
            if filter_value == "True":
                filter_value = 1
            
            elif filter_value == "False":
                filter_value = 0

            request = repository.select_by_status(status=filter_value)


        if request is False:
            return {"status": "error", "response": "", "message": "Nenhum usuário encontrado!"}
        
        elif request is None:
            return {"status": "error", "response": "", "message": "Erro ao tentar encontrar usuários no banco de dados!"}
        
        if filter_column == "ID":
            filter_column = "user_id"
        
        if filter_column == "Nome":
            filter_column = "user_name"

        if filter_column == "Email":
            filter_column = "user_email"

        if filter_column == "Admin":
            filter_column = "user_admin"

        if filter_column == "Status":
            filter_column = "user_status"
                        
        filter = {"column": f"{filter_column}", "value": f"{filter_value}"}
        request = repository.update(filter=filter, name=name, email=email, password=password, admin=admin, status=status)

        if request is False:
            return {"status": "error", "response": "", "message": "Erro ao tentar atualizar usuário no banco de dados!"}
        
        return {"status": "success", "response": "", "message": "Usuário atualizado com sucesso!"}

        
    def __validate_string_to_float_conversion(self, data: str) -> bool:
        try:
            float(data)
            return False
        
        except:
            return True
        
    def __validate_string_to_integer_conversion(self, data: str) -> bool:
        try:
            int(data)
            return False
        
        except:
            return True
    
    def __validate_email(self, email: str) -> bool:

        if email.count("@") != 1 or email.count(".") < 1:
            return True
        
        return False
    
    def __validate_email_exists(self, email:str) -> bool:

        request = UsersRepository(ConnectionMysqlDB()).select_by_email(email=email)

        if request is False:
            return False
        
        if request is None:
            return None
        
        return True


    def __validate_string_limit(self, data:str, limit:int) -> bool:
       return len(data) > limit
    
    def __validate_string_minimum(self, data:str, minimum:int) -> bool:
        return len(data) < minimum
    
    def __validate_passwords(self, password: str, confirm_password: str) -> bool:
        return password != confirm_password
    
    def __convert_string_to_date(self, date: str) -> datetime:
        if "/" in date:
            date = date.replace("/", "-")

        count_char = 0
        for number in date:
            if number == "-":
                break

            count_char += 1

        if count_char == 2:
            date_split = date.split("-")
            date = f"{date_split[2]}-{date_split[1]}-{date_split[0]}"

        return datetime.strptime(date, "%Y-%m-%d").date()
        
    def __validate_date(self, date:str) -> bool:
        try:
            if "/" in date:
                date = date.replace("/", "")
            
            elif "-" in date:
                date = date.replace("-", "")

            if date.isdigit() and len(date) == 8:
                return False
            
            else:
                return True
        
        except:
            return True
        
    def __validade_dates(self, date_rental: datetime, date_return: datetime) -> bool:

        if int(date_rental.year) > int(date_return.year):
            return True
        
        elif int(date_rental.month) > int(date_return.month) and int(date_rental.year) == int(date_return.year):
            return True
        
        elif int(date_rental.day) > int(date_return.day) and int(date_rental.month) == int(date_return.month) and int(date_rental.year) == int(date_return.year):
            return True
        
        return False