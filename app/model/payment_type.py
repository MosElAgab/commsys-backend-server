from app.db import db


class PaymentType(db):
    def __init__(self):
        super().__init__()

    def fetch_all_payment_type(self) -> list:
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM payment_type;")
        payment_type_list = cur.fetchall()
        cur.close()
        conn.close()
        return payment_type_list

    def get_payment_type_by_id(self, id: int) -> tuple:
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM payment_type WHERE payment_type_id=%s;", (id,))
        payment_type = cur.fetchall()
        cur.close()
        conn.close()
        return payment_type[0]

    def add_new_payment_type(self, new_payment_type: dict) -> tuple:
        payment_type_name = new_payment_type['payment_type_name']
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO payment_type "
                    "(payment_type_name) "
                    "VALUES"
                    ""
                    "(%s)"
                    "RETURNING *;",
                    (payment_type_name, ))
        added_payment_type = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return added_payment_type[0]
