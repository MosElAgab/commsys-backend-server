import psycopg2

class db():
    def __init__(self):
        self.database = 'test_commsys'
        self.user = ''
        self.password = ''
    
    def connect(self):
        conn = psycopg2.connect(
        database = self.database,
        user = self.user,
        password = self.password
        )
        return conn
    
    def hi(self):
        return 'hi'
