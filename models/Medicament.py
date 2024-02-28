from models.Product import Product

# Class Medicament
#(self, name, price, categorie, reference, date_Exp)
# attribut spécifique: indication
class Medicament(Product):
    def __init__(self, nom, prix, categorie, reference, date_Exp, utilisation):
        super().__init__(nom, prix, categorie, reference, date_Exp)
        self.utilisation = utilisation

    def get_utilisation(self):
        return self.utilisation

    def set_utilisation(self, utilisation):
        self.utilisation = utilisation

    def get_description(self):
        return f"Medicament: {self.get_nom()}, Price: {self.get_prix()},Categorie: {self.get_categorie()} ,Reference: {self.get_reference()}, Date_Expiration: {self.get_date_Exp()}, utilisation: {self.get_utilisation()}"
