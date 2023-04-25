class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def set_longueur(self):
        self.__longueur = int(input("Veuillez renseigner la longueur: "))
        while not self.__longueur > 0:
            self.__longueur = int(input("Veuillez renseigner une longueur valide: "))
        else:
            return self.__longueur

    def get_longueur(self):
        return self.__longueur

    def set_largeur(self):
        self.__largeur = int(input("Veuillez renseigner la largeur: "))
        while not self.__largeur > 0:
            self.__largeur = int(input("Veuillez renseigner une largeur valide: "))
        else:
            return self.__largeur

    def get_largeur(self):
        return self.__largeur

    def perimetre(self):
        add = self.__longueur + self.__largeur
        perimetre = add * 2
        return perimetre

    def surface(self):
        surface = self.__longueur * self.__largeur
        return surface


rectangle = Rectangle(0, 0)
rectangle.set_longueur()
rectangle.set_largeur()
print("La longueur du rectangle est de", rectangle.get_longueur(), "cm.")
print("La largeur du rectangle est de", rectangle.get_largeur(), "cm.")
print("Le périmètre du rectangle est de", rectangle.perimetre(), "cm.")
print("La surface du rectangle est de", rectangle.surface(), "cm².")


class Parallelepipede(Rectangle):
    def __init__(self, hauteur, longueur, largeur):
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur = hauteur

    def set_hauteur(self):
        self.__hauteur = int(input("Veuillez renseigner la hauteur du parallélépipède: "))
        while not self.__hauteur > 0:
            self.__hauteur = int(input("Veuillez renseigner une hauteur valide: "))
        else:
            return self.__hauteur

    def get_hauteur(self):
        return self.__hauteur

    def volume(self):
        volume = rectangle.get_longueur() * rectangle.get_largeur() * self.__hauteur
        return volume


parallelepipede = Parallelepipede(0, 0, 0)
parallelepipede.set_longueur()
parallelepipede.set_largeur()
parallelepipede.set_hauteur()
print("La hauteur du parallélépipède est de", parallelepipede.get_hauteur(), "cm.")
print("Le volume du parallélépipède est de", parallelepipede.volume(), "cm3.")
