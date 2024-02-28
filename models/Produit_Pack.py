from models.Product import Product

# name, price, categorie, reference, date_Exp)
# Class Produit_Pack
class Produit_Pack(Product):
    def __init__(self, nom, prix, categorie, reference, date_Exp, pack_quantity):
        super().__init__(nom, prix, categorie, reference, date_Exp)
        self.pack_qunatity = pack_quantity


    def get_pack_quantity(self):
        return self.pack_qunatity

    def set_size(self, pack_quantity):
        self.pack_qunatity = pack_quantity

    def get_description(self):
        return f"Produit_Pack: {self.get_nom()}, Price: {self.get_prix()},Categorie: {self.get_categorie()} ,Reference:{self.get_reference()}, Date_Expiration: {self.get_date_Exp()}, Pack_qté: {self.get_pack_quantity()}"
