from models.Product import Product

class ClothingProduct(Product):
    def __init__(self, name, price, reference, size):
        super().__init__(name, price, reference)
        self.size = size

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def get_description(self):
        return f"Product: {self.get_name()}, Price: {self.get_price()}, Reference: {self.get_reference()}, Size: {self.get_size()}"
