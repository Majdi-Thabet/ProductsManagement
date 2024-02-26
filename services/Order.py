from services.Cart import Cart


class Order(Cart):
    def __init__(self, capacity):
        self.products = []
        self.capacity = capacity
        self.size = 0

    def add_product(self, product):
        if self.size < self.capacity:
            if self.find_product(product) == -1:
                self.products.append(product)
                self.size += 1
            else:
                print("Cannot add 2 products with the same reference")
        else:
            print("Cannot add more products")

    def remove_product(self, product):
        index = self.find_product(product)
        if index != -1:
            del self.products[index]
            self.size -= 1
            return True
        else:
            print("Product not found in the order")
            return False

    def display_products(self):
        if self.size == 0:
            print("No Product")
        else:
            for product in self.products:
                print(product.get_description())

    def total(self):
        total_sum = sum(product.get_price() for product in self.products)
        return total_sum

    def find_product(self, product):
        for i, p in enumerate(self.products):
            if p.get_reference() == product.get_reference():
                return i
        return -1
