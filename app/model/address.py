from app.db import db


class Address(db):
    def __init__(self):
        super().__init__()

    def fetch_all_address(self) -> list:
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM address;")
        address_list = cur.fetchall()
        cur.close()
        conn.close()
        return address_list

    def get_address_by_id(self, id: int) -> list:
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM address WHERE address_id=%s;", (id,))
        address = cur.fetchall()
        cur.close()
        conn.close()
        return address[0]

    def add_new_address(self, new_address: dict) -> tuple:
        first_line = new_address['first_line']
        second_line = new_address['second_line']
        district = new_address['district']
        city = new_address['city']
        postal_code = new_address['postal_code']
        country = new_address['country']
        phone = new_address['phone']
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO address "
                    "(first_line, second_line, district, city, postal_code, country, phone) "
                    "VALUES"
                    ""
                    "(%s, %s, %s, %s, %s, %s, %s)"
                    "RETURNING *;",
                    (first_line, second_line, district, city, postal_code, country, phone))
        added_address = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return added_address[0]
