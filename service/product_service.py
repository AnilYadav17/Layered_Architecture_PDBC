from dao.product_dao import ProductDao

class ProductService:
    def display_all_products(self):
        print("Processing product information...")
        d1 = ProductDao()
        products = d1.get_all_products()
        return products

    def add_product(self, product):
        print("Service adding new product...")
        d1 = ProductDao()
        d1.save_product(product)

    def search_product_by_id(self, pid):
        d1 = ProductDao()
        product = d1.get_product_by_id(pid)
        return product

    def update_product_by_id(self, pid, name, price):
        d1 = ProductDao()
        rows = d1.update_product_by_id(pid, name, price)
        return rows

    def delete_product_by_id(self, pid):
        d1 = ProductDao()
        rows = d1.delete_product_by_id(pid)
        return rows
