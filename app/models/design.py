from flask import request, jsonify
from app.connection import DatabaseConnector
from flask_restful import Resource

class Design(Resource):
    def get(self, id):
        db = DatabaseConnector()
        conn = db.conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM design WHERE design_id=%s;", (id,))
        row = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(row)
    
    # def get(self):
    #     db = DatabaseConnector()
    #     conn = db.conn()
    #     cur = conn.cursor()
    #     cur.execute("SELECT * FROM design;")
    #     rows = cur.fetchall()
    #     cur.close()
    #     conn.close()
    #     return jsonify(rows)

    def post(self):
        data = request.get_json()
        # design_id = data['design_id']
        design_name = data['design_name']
        file_location = data['file_location']
        file_name = data['file_name']
        # print(design_id, file_name, file_location, file_name)
        db = DatabaseConnector()
        conn = db.conn()
        cur = conn.cursor()
        cur.execute("INSERT INTO design "
                    "(created_at, last_updated, design_name, file_location, file_name) "
                    "VALUES"
                    "(CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, %s, %s, %s)"
                    "RETURNING *;", 
                    (design_name, file_location, file_name))
        returned = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(returned)

