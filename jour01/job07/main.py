class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages

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


livre = Livre("", "", 0)

livre.set_titre()

livre.set_auteur()

livre.set_pages()

print("Le titre du livre est", livre.get_titre())
print("L'auteur du livre est", livre.get_auteur())
print("Le nombre de pages est de", livre.get_pages())
