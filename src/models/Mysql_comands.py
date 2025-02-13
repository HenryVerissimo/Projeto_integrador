from conexao_model import DatabaseMysql, conexao

class InsertDatabase:

    def __init__(self, conexao: DatabaseMysql):
        self.__conexao = conexao

    def insert_usuario(self, funcionario: str, cidade: str, salario: float, data_contratacao: str) -> None:
        try:
            self.__conexao.connect()
            cursor = self.__conexao.connection.cursor()
            sql = f"INSERT INTO funcionarios (funcionario, cidade, salario, data_contratacao)\
                VALUES ('{funcionario}', '{cidade}', '{salario}', '{data_contratacao}');"
            
            cursor.execute(sql)
            self.__conexao.connection.commit()
        
        except Exception as e:
            print(f"Ocorreu o erro: {e}")

        finally:
            if cursor:
                cursor.close()
            self.__conexao.close_connection()

#InsertDatabase(conexao).insert_usuario("Lucas", "Barrinha", 1500, "2005-12-12")