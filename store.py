import products

class Store:
    def __init__(self, products=None):
        self.products = list(products) if products else []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        return len(self.products)

    def get_all_products(self):
        list_of_active_products = []
        for product in self.products:
            if product.is_active():
                list_of_active_products.append(product)
        return list_of_active_products

    def order(self, shopping_list):
        total_price_list = []
        for product, quantity in shopping_list:
            total_price_per_product = product.buy(quantity)
            total_price_list.append(total_price_per_product)
        return sum(total_price_list)
