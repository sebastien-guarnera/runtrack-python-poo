class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        print(self.__longueur)

    def set_longueur(self):
        self.__longueur = 15
        return self.__longueur

    def get_largeur(self):
        print(self.__largeur)

    def set_largeur(self):
        self.__largeur = 7
        return self.__largeur


rectangle = Rectangle(10, 5)

rectangle.get_longueur()
rectangle.set_longueur()
rectangle.get_longueur()

rectangle.get_largeur()
rectangle.set_largeur()
rectangle.get_largeur()
