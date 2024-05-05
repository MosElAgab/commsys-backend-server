import psycopg2

class DatabaseConnector():
    def __init__(self):
        self.database = 'test_commsys'
        self.user = ''
        self.password = ''
    
    def conn(self):
        conn = psycopg2.connect(
        database = self.database,
        user = self.user,
        password = self.password
        )
        return conn
