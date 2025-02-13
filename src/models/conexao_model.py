import mysql.connector
from mysql.connector import Error


class DatabaseMysql():

    def __init__(self, host, user, password, database) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self) -> None:
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        
            if self.connection.is_connected():
                print("Conexão bem sucedida ao banco de dados.")

        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")


    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexão fechada.")


conexao = DatabaseMysql('192.168.120.154', 'root', 'ubuntu', 'empresa')



