import mysql.connector
from time import sleep

#conexão com o banco de dados
class ConexaoMysql:
    def __init__(self, host, user, password, port):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.conexao = None


    def conectar_banco(self):
        try:
            if self.conexao.is_connected():
                self.fechar_conexao()
     
            self.conexao = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                port = self.port )
            
        except Exception:
            print("A conexão falhou! Tentando estabelecer nova conexão")
            sleep(5)
            self.conectar_banco()


    def fechar_conexao(self):
        if self.conexao.is_connected():
            self.conexao.close()
            self.conexao = None


conexao1 = ConexaoMysql("#ip servidor", "User", "Senha123", "3306")
