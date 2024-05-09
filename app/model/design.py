from app.db import db


class Design(db):
    def __init__(self):
        super().__init__()

    def fetch_all_design(self):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM design;")
        design_list = cur.fetchall()
        cur.close()
        conn.close()
        return design_list

    def get_design_by_id(self, id):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM design WHERE design_id=%s;", (id,))
        desing = cur.fetchall()
        cur.close()
        conn.close()
        return desing[0]

    def add_new_design(self, new_design):
        design_name = new_design['design_name']
        file_location = new_design['file_location']
        file_name = new_design['file_name']
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO design "
                    "(created_at, last_updated, design_name, file_location, file_name) "
                    "VALUES"
                    "(CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, %s, %s, %s)"
                    "RETURNING *;",
                    (design_name, file_location, file_name))
        added_design = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return added_design[0]
