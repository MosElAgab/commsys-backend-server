from app.db import db


class Counterparty(db):
    def __init__(self):
        super().__init__()

    def fetch_all_counterparty(self) -> list:
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM counterparty;")
        counterparty_list = cur.fetchall()
        cur.close()
        conn.close()
        return counterparty_list

    def get_counterparty_by_id(self, id: int) -> tuple:
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM counterparty WHERE counterparty_id=%s;", (id,))
        counterparty = cur.fetchall()
        cur.close()
        conn.close()
        return counterparty[0]

    def add_new_counterparty(self, new_counterparty: dict) -> tuple:
        counterparty_legal_name = new_counterparty['counterparty_legal_name']
        legal_address_id = new_counterparty['legal_address_id']
        commercial_contact = new_counterparty['commercial_contact']
        delivery_contact = new_counterparty['delivery_contact']
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO counterparty "
                    "(counterparty_legal_name, legal_address_id, commercial_contact, delivery_contact)"
                    "VALUES"
                    "(%s, %s, %s, %s) "
                    "RETURNING *;",
                    (counterparty_legal_name, legal_address_id, commercial_contact, delivery_contact))
        added_counterparty = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return added_counterparty[0]
