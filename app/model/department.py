from app.db import db


class Department(db):
    def __init__(self):
        super().__init__()

    def fetch_all_department(self) -> list:
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM department;")
        department_list = cur.fetchall()
        cur.close()
        conn.close()
        return department_list

    def get_department_by_id(self, id: int) -> tuple:
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM department WHERE department_id=%s;", (id,))
        department = cur.fetchall()
        cur.close()
        conn.close()
        return department[0]

    def add_new_department(self, new_department: dict) -> tuple:
        department_name = new_department['department_name']
        location = new_department['location']
        manager = new_department['manager']
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO department "
                    "(department_name, location, manager) "
                    "VALUES"
                    ""
                    "(%s, %s, %s)"
                    "RETURNING *;",
                    (department_name, location, manager))
        added_department = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return added_department[0]
