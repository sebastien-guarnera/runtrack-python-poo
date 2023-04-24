class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def age(self):
        print(self.age)

    def vieillir(self):
        self.age += 1
        return self.age

    def nommer(self):
        self.prenom = "luna"
        return self.prenom


animal = Animal()

print("L'age de l'animal est", animal.age)

print("L'age de l'animal est", animal.vieillir())

print("L'animal se nomme", animal.nommer())
