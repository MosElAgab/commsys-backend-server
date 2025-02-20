from app.db import db


class PurchaseOrder(db):
    def __init__(self):
        super().__init__()

    def fetch_all_purchase_order(self) -> list:
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM purchase_order;")
        purchase_order_list = cur.fetchall()
        cur.close()
        conn.close()
        return purchase_order_list

    def get_purchase_order_by_id(self, id: int) -> tuple:
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM purchase_order WHERE purchase_order_id=%s;", (id,))
        purchase_order = cur.fetchall()
        cur.close()
        conn.close()
        return purchase_order[0]

    def add_new_purchase_order(self, new_purchase_order: dict) -> tuple:
        staff_id = new_purchase_order['staff_id']
        counterparty_id = new_purchase_order['counterparty_id']
        item_code = new_purchase_order['item_code']
        item_quantity = new_purchase_order['item_quantity']
        item_unit_price = new_purchase_order['item_unit_price']
        currency_id = new_purchase_order['currency_id']
        agreed_delivery_date = new_purchase_order['agreed_delivery_date']
        agreed_payment_date = new_purchase_order['agreed_payment_date']
        agreed_delivery_location_id = new_purchase_order['agreed_delivery_location_id']
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO purchase_order "
                    "(staff_id, counterparty_id, item_code, item_quantity, item_unit_price, currency_id, "
                    "agreed_delivery_date, agreed_payment_date, agreed_delivery_location_id)"
                    "VALUES"
                    "(%s, %s, %s, %s, %s, %s, %s, %s, %s) "
                    "RETURNING *;",
                    (staff_id, counterparty_id, item_code, item_quantity, item_unit_price, currency_id,
                     agreed_delivery_date, agreed_payment_date, agreed_delivery_location_id))
        added_purchase_order = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return added_purchase_order[0]
