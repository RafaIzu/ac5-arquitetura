import sqlalchemy


class CheckConnection:
    def __init__(self, connection_test, sql_connection):
        self.__connection_test = connection_test
        self.__sql_connection = sql_connection

    def create_database_ac5(self):
        engine = sqlalchemy.create_engine(self.__sql_connection)
        conn = engine.connect()
        conn.execute("commit")
        conn.execute("create database ac5")
        conn.close()

    def check_connection(self):
        engine = sqlalchemy.create_engine(self.__connection_test)

        try:
            conn = engine.connect()
            conn.close()
            
        except:
            print("criando banco de dados...")
            self.create_database_ac5()
            print("Criado!")

        else:
            print("conectado")
