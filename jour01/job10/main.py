class Voiture:
    def __init__(self, marque, modele, annee, km):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__km = km
        self.en_marche = False

    def set_marque(self):
        self.__marque = input("Renseignez la marque: ")

    def get_marque(self):
        print("La marque du véhicule est", self.__marque)

    def set_modele(self):
        self.__modele = input("Renseignez le modèle: ")

    def get_modele(self):
        print("Le modèle du véhicule est", self.__modele)

    def set_annee(self):
        self.__annee = input("Renseignez l'année de conception: ")

    def get_annee(self):
        print("Le véhicule a été construit en", self.__annee)

    def set_km(self):
        self.__km = input("Renseignez le nombre de kilomètres: ")

    def get_km(self):
        print("Le compteur du véhicule affiche", self.__km, "kilomètres")

    def demarrer(self):
        if not self.en_marche:
            self.en_marche = True
            print("Le véhicule est désormais allumé")
        else:
            print("Le véhicule est déjà allumé.")

    def arreter(self):
        if self.en_marche:
            self.en_marche = False
            print("Le vehicule est désormais éteint")
        else:
            print("Le véhicule est déjà éteint.")


voiture = Voiture("", "", "", "")

voiture.set_marque()
voiture.set_modele()
voiture.set_annee()
voiture.set_km()
voiture.get_marque()
voiture.get_modele()
voiture.get_annee()
voiture.get_km()
voiture.demarrer()
voiture.arreter()

