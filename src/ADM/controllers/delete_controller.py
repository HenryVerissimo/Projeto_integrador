from src.WEB.model.config import ConnectionMysqlDB
from src.WEB.model.repository import GameRentalRepository, UsersRepository, GamesRepository
from src.WEB.model.entities import Users, GameRental, Games


class DeleteRepository:

    def delete_user(self, id)