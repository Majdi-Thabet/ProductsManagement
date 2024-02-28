from models.Product import Product
from services.Cart import Cart


class Medicament(Product):

    def __init__(self, nom, prix, categorie, reference, date_Exp, utilisation):
        self.nom = nom
        self.prix = prix
        self.categorie = categorie
        self.reference = reference
        self.date_Exp = date_Exp
        self.utilisation = utilisation

    def __str__(self):
        return f"{self.nom}, {self.prix}, {self.categorie}, {self.reference}, {self.date_Exp}, {self.utilisation}"


class Produit_Pack(Product):
    def __init__(self, nom, prix, categorie, reference, date_Exp, pack_quantity):
        self.nom = nom
        self.prix = prix
        self.categorie = categorie
        self.reference = reference
        self.date_Exp = date_Exp
        self.pack_quantity = pack_quantity

    def __str__(self) -> str:
        return self.get_description()

    def get_description(self):
        return f"Medicament: {self.get_nom()}, Price: {self.get_prix()},Categorie: {self.get_categorie()} ,Reference: {self.get_reference()}, Date_Expiration: {self.get_date_Exp()}"


class Order:
    def __init__(self, max_products):
        self.max_products = max_products
        self.products = []

    def ajouter_produit(self, product):
        if len(self.products) < self.max_products:
            self.products.append(product)
        else:
            print("Cart is full.")

    def supprimer_produit(self, reference):
        for product in self.products:
            if product.reference == reference:
                self.products.remove(product)
                print("Produit supprimé.")
                break
        else:
            print("Produit non trouvé.")

    def afficher_produits(self):
        for product in self.products:
            print(product)

    def total(self):
        total = 0
        for product in self.products:
            total += product.prix
        return total


def display_main_menu():
    print("\nMain Menu:")
    print("1. Ajouter Produit")
    print("2. Afficher Produit")
    print("3. Total")
    print("4. Supprimer Produit")
    print("5. Exit")


def display_product_menu(product_type):
    print(f"\n{product_type} :")
    print("1. Ajouter un nouveau produit")
    print("2. Retour au Menu Principal ")


def main():
    cart = Order(5)

    while True:
        display_main_menu()
        main_choice = input("Entrer votre choix (1-5): ")

        if main_choice == "1":
            print("\nChoisir le type du produitt:")
            print("1. Medicament")
            print("2. Produit_Pack")
            product_type_choice = input("Entrer votre choix (1-2): ")

            if product_type_choice == "1":
                display_product_menu("Bienvenue Dans Le Menu de Medicament")
                nom = input("Entrer le nom de médicament: ")
                prix = float(input("Entrer le prix de médicament: "))
                categorie = input("Entrer la categorie de medicament: ")
                reference = input("Entrer la reférence de Medicament: ")
                date_Exp = input("Entrer la date d'expiration: ")
                utilisation = input("Entrer les détails d'utilisation de Médicament: ")

                cart.ajouter_produit(
                    Medicament(nom, prix, categorie, reference, date_Exp, utilisation)
                )

            elif product_type_choice == "2":
                display_product_menu("Bienvenu au Menu De Produit_Pack")
                nom = input("Entrer le nom du Produit_Pack: ")
                prix = float(input("Entrer le prix du Produit_Pack: "))
                categorie = input("Entrer la categorie du produit: ")
                reference = input("Entrer la réference du Produit_Pack: ")
                date_Exp = input("Entrer la date d'expiration: ")
                pack_quantity = int(input("Enter la quantité de ce produit_pack: "))

                cart.ajouter_produit(
                    Produit_Pack(
                        nom, prix, categorie, reference, date_Exp, pack_quantity
                    )
                )

            else:
                print("Invalid choix. Please entrer 1 ou 2.")

        elif main_choice == "2":
            print("\nProduct list:")
            cart.afficher_produits()

        elif main_choice == "3":
            print("\nTotal: ${:.2f}".format(cart.total()))

        elif main_choice == "4":
            reference = input("Entrer la reference du produit à supprimer: ")
            cart.supprimer_produit(reference)

        elif main_choice == "5":
            print("Quitter le programme")
            break

        else:
            print("Invalide choix. Entrer un nombre de 1 1 à 5.")


if __name__ == "__main__":
    main()
