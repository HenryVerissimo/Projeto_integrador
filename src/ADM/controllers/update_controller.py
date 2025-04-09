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
    
    def update_game(self, name: str, price: str, quantity: str, genre: str, description: str, filter_column: str, filter_value: str) -> dict:

        repository = GamesRepository(ConnectionMysqlDB())

        if not filter_value:
            return {"status": "error", "response": "", "message": "Forneça um parâmetro para filtragem!"}
        
        if name is None and price is None and quantity is None and genre is None and description is None:
            return {"status": "error", "response": "", "message": "Forneça um parâmetro para atualização!"}
        
        if name:
            name = name.strip()
            if self.__validate_string_limit(name, 100):
                return {"status": "error", "response": "", "message": "O nome do jogo precisa ter menos de 100 caracteres!"}

        if price:
            price = price.strip()
            price = self.__convert_comma_to_period(price)
            if self.__validate_string_to_float_conversion(price):
                return {"status": "error", "response": "", "message": "Preço precisa ser um número!"}
            
            if self.__validate_negative_number(price):
                return {"status": "error", "response": "", "message": "Preço nao pode ser negativo!"}
            
        if quantity:
            quantity = quantity.strip()
            if self.__validate_string_to_integer_conversion(quantity):
                return {"status": "error", "response": "", "message": "Quantidade precisa ser um número!"}
            
            if self.__validate_negative_number(quantity):
                return {"status": "error", "response": "", "message": "Quantidade nao pode ser negativa!"}
            
        if genre:
            genre = genre.strip()
            if self.__validate_string_limit(genre, 100):
                return {"status": "error", "response": "", "message": "O gênero do jogo precisa ter menos de 100 caracteres!"}
            
        if description:
            description = description.strip()

        if filter_column == "ID":
            filter_column = "game_id"
        
        if filter_column == "Nome":
            filter_column = "game_name"

        if filter_column == "Preço":
            filter_column = "game_price"

        if filter_column == "Quantidade":
            filter_column = "game_quantity"

        if filter_column == "Gênero":
            filter_column = "game_genre"

        if filter_column == "Descrição":
            filter_column = "game_description"
        
        filter = {"column": f"{filter_column}", "value": f"{filter_value}"}
        request = repository.update(filter=filter, name=name, price=price, quantity=quantity, genre=genre, description=description)

        if request is False:
            return {"status": "error", "response": "", "message": "Erro ao tentar atualizar jogo no banco de dados!"}
        
        return {"status": "success", "response": "", "message": "Jogo atualizado com sucesso!"}
    
    def update_rental(self, user_id: str, game_id: str, rental_date:str, return_date: str, filter_column: str, filter_value: str) -> dict:

        repository = GameRentalRepository(ConnectionMysqlDB())

        if not filter_value:
            return {"status": "error", "response": "", "message": "Forneça um parâmetro para filtragem!"}
        
        if user_id is None and game_id is None and rental_date is None and return_date is None:
            return {"status": "error", "response": "", "message": "Forneça um parâmetro para atualização!"}
        
        if user_id:
            user_id = user_id.strip()
            if self.__validate_string_to_integer_conversion(user_id):
                return {"status": "error", "response": "", "message": "ID do usuário precisa ser um número!"}
            
            if self.__validate_negative_number(user_id):
                return {"status": "error", "response": "", "message": "ID do usuário nao pode ser negativo!"}
            
            if self.__validate_user_exists(user_id) is False:
                return {"status": "error", "response": "", "message": "Nenhum usuário encontrado com esse ID!"}
            
            if self.__validate_user_exists(user_id) is None:
                return {"status": "error", "response": "", "message": "Erro ao tentar verificar se o ID do usuário é valido!"}
            
        if game_id:
            game_id = game_id.strip()
            if self.__validate_string_to_integer_conversion(game_id):
                return {"status": "error", "response": "", "message": "ID do jogo precisa ser um número!"}
            
            if self.__validate_negative_number(game_id):
                return {"status": "error", "response": "", "message": "ID do jogo nao pode ser negativo!"}
            
            if self.__validate_game_exists(game_id) is False:
                return {"status": "error", "response": "", "message": "Nenhum jogo encontrado com esse ID!"}
            
            if self.__validate_game_exists(game_id) is None:
                return {"status": "error", "response": "", "message": "Erro ao tentar verificar se o ID do jogo é valido!"}
            
        if rental_date:
            rental_date = rental_date.strip()
            if self.__validate_date(rental_date):
                return {"status": "error", "response": "", "message": "Data de aluguel precisa ser uma data válida!"}
            
        if return_date:
            return_date = return_date.strip()
            if self.__validate_date(return_date):
                return {"status": "error", "response": "", "message": "Data de entrega precisa ser uma data válida!"}
            
        rental_date = self.__convert_string_to_date(rental_date)
        return_date = self.__convert_string_to_date(return_date)
            
        if filter_column == "ID":
            filter_column = "game_rental_id"

        elif filter_column == "Usuário":
            filter_column = "user_id"

        elif filter_column == "Jogo":
            filter_column = "game_id"

        elif filter_column == "Data de aluguel":
            filter_column = "game_rental_date"

        elif filter_column == "Data de entrega":
            filter_column = "game_return_date"
        
        filter = {"column": f"{filter_column}", "value": f"{filter_value}"}
        request = repository.update(filter=filter, user_id=user_id, game_id=game_id, game_rental_date=rental_date, game_return_date=return_date)

        if request is False:
            return {"status": "error", "response": "", "message": "Erro ao tentar atualizar jogo no banco de dados!"}
        
        return {"status": "success", "response": "", "message": "Jogo alugado com sucesso!"}
            
        
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
        
    def __convert_comma_to_period(self, data: str) -> str:

        if "," in data:
            data = data.replace(",", ".")

        return data
    
    def __validate_negative_number(self, data: str) -> bool:
        data = float(data)
        return data < 0
        
    
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
    
    def __validate_user_exists(self, user_id: str) -> bool:

        repository = UsersRepository(ConnectionMysqlDB())
        request = repository.select_by_id(id=user_id)

        if request is False:
            return False
        
        if request is None:
            return None
        
        return True
    
    def __validate_game_exists(self, game_id: str) -> bool:

        repository = GamesRepository(ConnectionMysqlDB())
        request = repository.select_by_id(id=game_id)

        if request is False:
            return False
        
        if request is None:
            return None
        
        return True


    def __validate_string_limit(self, data:str, limit:int) -> bool:
       return len(data) > limit
    
    def __validate_string_minimum(self, data:str, minimum:int) -> bool:
        return len(data) < minimum
    
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