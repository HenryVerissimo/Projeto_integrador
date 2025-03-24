from src.model.repository.users_repository import UsersRepository
from src.model.config.connection_database import ConnectionMysqlDB

repo = UsersRepository(ConnectionMysqlDB())
repo.insert("Rafael", "Rafa@gmail.com", "senha123")
