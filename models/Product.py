class Product:
    def __init__(self, name, price, reference):
        self.name = name
        self.price = price
        self.reference = reference

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_reference(self):
        return self.reference

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def set_reference(self, reference):
        self.reference = reference

    def get_description(self):
        pass
