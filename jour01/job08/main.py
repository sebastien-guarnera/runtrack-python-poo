class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponible = True

    def set_titre(self):
        self.__titre = input("Renseignez le titre du livre: ")

    def get_titre(self):
        return self.__titre

    def set_auteur(self):
        self.__auteur = input("Renseignez le nom de l'auteur: ")

    def get_auteur(self):
        return self.__auteur

    def set_pages(self):
        self.__pages = input("Renseignez le nombre de pages: ")
        while not self.__pages.isnumeric():
            self.__pages = input("Erreur, veuillez entrer un entier: ")
        else:
            return self.__pages

    def get_pages(self):
        return self.__pages

    def get_verification(self):
        return self.__disponible

    def set_emprunter(self):
        if self.__disponible:
            print("Ce livre est disponible à l'emprunt.")
            self.__disponible = False
            return self.__disponible
        else:
            print("Ce livre a déjà été emprunté.")

    def set_rendre(self):
        if not self.__disponible:
            print("Le livre est rendu.")
            self.__disponible = True
            return self.__disponible
        else:
            print("Ce livre n'a pas été emprunté.")


livre = Livre("", "", 0)

print(livre.get_verification())
livre.set_emprunter()
livre.set_rendre()
