from models.Product import Product


class ElectronicProduct(Product):
    def __init__(self, name, price, reference, power):
        super().__init__(name, price, reference)
        self.power = power

    def get_power(self):
        return self.power

    def set_power(self, power):
        self.power = power

    def get_description(self):
        return f"Electronic Product: {self.get_name()}, Price: {self.get_price()}, Reference: {self.get_reference()}, Power: {self.get_power()}"
