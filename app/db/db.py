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

    
    def seed_test_db(self):
        with open('./db/test_db/seed_test_db.sql', 'r') as f:
            conn = self.connect()
            cur = conn.cursor()
            cur.execute(f.read())
            cur.close()
            conn.commit()
            conn.close()
    