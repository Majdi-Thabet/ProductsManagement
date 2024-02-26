from models.BookProduct import BookProduct
from models.ClothingProduct import ClothingProduct
from models.ElectronicProduct import ElectronicProduct
from services.Order import Order

def display_menu():
    print("\nMenu:")
    print("1. Add Electronic Product")
    print("2. Add Clothing Product")
    print("3. Add Book Product")
    print("4. Display Products")
    print("5. Total")
    print("6. Remove Product")
    print("7. Exit")

def main():
    cart = Order(5)
    cart.add_product(ElectronicProduct("Printer", 755.0, "1524", 8.0))
    cart.add_product(ClothingProduct("Pants", 39.99, "7568", "Large"))
    cart.add_product(BookProduct("java", 55.99, "10568", "demo"))

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            name = input("Enter Electronic Product name: ")
            price = float(input("Enter Electronic Product price: "))
            reference = input("Enter Electronic Product reference: ")
            power = float(input("Enter Electronic Product power: "))
            cart.add_product(ElectronicProduct(name, price, reference, power))
        elif choice == "2":
            name = input("Enter Clothing Product name: ")
            price = float(input("Enter Clothing Product price: "))
            reference = input("Enter Clothing Product reference: ")
            size = input("Enter Clothing Product size: ")
            cart.add_product(ClothingProduct(name, price, reference, size))
        elif choice == "3":
            name = input("Enter Book Product name: ")
            price = float(input("Enter Book Product price: "))
            reference = input("Enter Book Product reference: ")
            author = input("Enter Book Product author: ")
            cart.add_product(BookProduct(name, price, reference, author))
        elif choice == "4":
            print("\nProduct list:")
            cart.display_products()
        elif choice == "5":
            print("\nTotal: ${:.2f}".format(cart.total()))
        elif choice == "6":
            reference = input("Enter the reference of the product to remove: ")
            cart.remove_product(BookProduct("", 0.0, reference, ""))  # Dummy BookProduct for reference
        elif choice == "7":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

if __name__ == "__main__":
    main()
