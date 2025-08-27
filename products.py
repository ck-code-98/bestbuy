class Product:
    def __init__(self, name, price, quantity):

        if not isinstance(name, str) or not name.strip():
            raise ValueError("Product name must be a string and not empty!")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number!")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer!")

        self.active = True
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity <= 0:
            self.active = False

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price} $, Quantity: {self.quantity}")

    def buy(self, quantity):
        try:
            total_price = quantity * self.price
            if quantity > self.quantity:
                raise ValueError
            self.quantity -= quantity
            if self.quantity <= 0:
                self.deactivate()
            return total_price
        except ValueError:
            print("Not enough product left in stock!")
            return None
