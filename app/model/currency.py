from app.db import db


class Currency(db):
    def __init__(self):
        super().__init__()

    def fetch_all_currency(self) -> list:
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM currency;")
        currency_list = cur.fetchall()
        cur.close()
        conn.close()
        return currency_list

    def get_currency_by_id(self, id: int) -> tuple:
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM currency WHERE currency_id=%s;", (id,))
        currency = cur.fetchall()
        cur.close()
        conn.close()
        return currency[0]

    def add_new_currency(self, new_currency: dict) -> tuple:
        currency_code = new_currency['currency_code']
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO currency "
                    "(currency_code) "
                    "VALUES"
                    ""
                    "(%s)"
                    "RETURNING *;",
                    (currency_code, ))
        added_currency = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return added_currency[0]
