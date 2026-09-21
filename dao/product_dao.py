from database.connection import Database
from model.product import Product

class ProductDao:
    def get_all_products(self):
        print("DAO retrieving all products...")
        db = Database()
        conn = db.connect()
        cursor = conn.cursor()
        query = "select pid, pname, price from product"
        cursor.execute(query)
        products = []
        for row in cursor.fetchall():
            product = Product(row[0], row[1], float(row[2]) if row[2] is not None else 0.0)
            products.append(product)
        conn.close()
        return products

    def save_product(self, product):
        print("DAO saving product data...")
        print(f"Product ID: {product.id}, Name: {product.name}, Price: {product.price}")
        db = Database()
        conn = db.connect()
        cursor = conn.cursor()
        query = "insert into product(pid, pname, price) values (%s, %s, %s)"
        data = (product.id, product.name, product.price)
        cursor.execute(query, data)
        conn.commit()
        conn.close()
        print("Product saved successfully!!")

    def get_product_by_id(self, pid):
        db = Database()
        conn = db.connect()
        cursor = conn.cursor()
        query = "select pid, pname, price from product where pid = %s"
        cursor.execute(query, (pid,))
        row = cursor.fetchone()
        conn.close()
        if row is not None:
            return Product(row[0], row[1], float(row[2]) if row[2] is not None else 0.0)
        return None

    def update_product_by_id(self, pid, name, price):
        db = Database()
        conn = db.connect()
        cursor = conn.cursor()
        query = "update product set pname = %s, price = %s where pid = %s"
        cursor.execute(query, (name, price, pid))
        conn.commit()
        rows = cursor.rowcount
        conn.close()
        return rows

    def delete_product_by_id(self, pid):
        db = Database()
        conn = db.connect()
        cursor = conn.cursor()
        query = "delete from product where pid = %s"
        cursor.execute(query, (pid,))
        rows = cursor.rowcount
        conn.commit()
        conn.close()
        return rows
