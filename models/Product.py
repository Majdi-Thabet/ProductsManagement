from datetime import datetime
class Product:
    def __init__(self, nom, prix, categorie, reference, date_Exp):
        self.nom = nom
        self.prix = prix
        self.categorie = categorie
        self.reference = reference

        self.date_Exp = datetime.strptime(date_Exp, '%d/%m/%Y')

    def get_nom(self):
        return self.nom

    def get_prix(self):
        return self.prix

    def get_categorie(self):
        return self.categorie

    def get_reference(self):
        return self.reference

    def get_date_Exp(self):
        return self.date_Exp

    def set_nom(self, nom):
        self.nom = nom

    def set_prix(self, prix):
        self.prix = prix

    def set_categorie(self, categorie):
        self.categorie = categorie

    def set_reference(self, reference):
        self.reference = reference

    def set_date_Exp(self, date_Exp):
        self.date_Exp = date_Exp
    def get_description(self):
        return f"Produit: {self.get_nom()}, Price: {self.get_prix()},Categorie: {self.get_categorie()} ,Reference: {self.get_reference()}, Date_Expiration: {self.get_date_Exp()}, utilisation: {self.get_utilisation()}"