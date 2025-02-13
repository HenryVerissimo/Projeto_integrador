import mysql.connector
from mysql.connector import Error

class DatabaseConnection:

    def __init__(self) -> None:
        self.host = '192.168.120.154'
        self.user = 'root'
        self.password = 'ubuntu'
        self.database = 'empresa'
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

    def incluir_usuario(self, funcionario, cidade, salario, data_contratacao) -> None:
        try:
            self.connect()
            cursor = self.connection.cursor()
            sql = f"INSERT INTO funcionarios (funcionario, cidade, salario, data_contratacao)\
                VALUES ('{funcionario}', '{cidade}', '{salario}', '{data_contratacao}');"
            
            cursor.execute(sql)
            self.connection.commit()
        
        except Error as e:
            print(f"Ocorreu o erro: {e}")

        finally:
            if cursor:
                cursor.close()
            self.close_connection()




conexao = DatabaseConnection()
conexao.incluir_usuario('Henrique', 'Jaboticabal', 1500, '2002-12-16')



