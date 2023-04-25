class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsvehicule(self):
        print("Marque =", self.marque)
        print("Modèle =", self.modele)
        print("Année =", self.annee)
        print("Prix =", self.prix)


class Voiture(Vehicule):
    def __init__(self, marque, annee, prix, modele, portes):
        super().__init__(marque, annee, prix, modele)
        self.portes = portes

    def informationsvehicule(self):
        print("Marque =", self.marque)
        print("Modèle =", self.modele)
        print("Année =", self.annee)
        print("Prix =", self.prix)
        print("Portes =", self.portes)


voiture = Voiture("Mercedes", "Classe A", 2018, 300000, 4)
voiture.informationsvehicule()

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2

    def informationsvehicule(self):
        print("Marque =", self.marque)
        print("Modèle =", self.modele)
        print("Année =", self.annee)
        print("Prix =", self.prix)
        print("Roues =", self.roues)


moto = Moto("Yamaha", "1200 Vmax", 1987, 4500)
moto.informationsvehicule()
