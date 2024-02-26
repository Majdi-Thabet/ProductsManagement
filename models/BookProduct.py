from models.Product import Product


class BookProduct(Product):
    def __init__(self, name, price, reference, author):
        super().__init__(name, price, reference)
        self.author = author

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_description(self):
        return f"Book Product: {self.get_name()}, Price: {self.get_price()}, Reference: {self.get_reference()}, Author: {self.get_author()}"
