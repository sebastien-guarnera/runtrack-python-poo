class Forme:
    def __init__(self, aire):
        self.aire = aire


forme = Forme(0)


class Rectangle(Forme):
    def __init__(self):
        Forme.__init__(self, Forme)
        self.largeur = 4
        self.longueur = 5

    def get_aire(self):
        aire = self.aire + (self.longueur * self.largeur)
        return aire


rectangle = Rectangle()
print(rectangle.get_aire())
