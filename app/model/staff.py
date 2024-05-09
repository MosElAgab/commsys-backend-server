from app.db import db


class Staff(db):
    def __init__(self):
        super().__init__()

    def fetch_all_staff(self) -> list:
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM staff;")
        staff_list = cur.fetchall()
        cur.close()
        conn.close()
        return staff_list

    def get_staff_by_id(self, id: int) -> tuple:
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM staff WHERE staff_id=%s;", (id,))
        staff = cur.fetchall()
        cur.close()
        conn.close()
        return staff[0]

    def add_new_staff(self, new_staff: dict) -> tuple:
        first_name = new_staff['first_name']
        last_name = new_staff['last_name']
        department_id = new_staff['department_id']
        email_address = new_staff['email_address']
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO staff "
                    "(first_name, last_name, department_id, email_address) "
                    "VALUES"
                    "(%s, %s, %s, %s) "
                    "RETURNING *;",
                    (first_name, last_name, department_id, email_address))
        added_staff = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return added_staff[0]
