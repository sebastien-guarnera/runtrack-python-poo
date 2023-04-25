class Personne:
    def __init__(self, entier):
        self.age = entier

    def afficher_age(self):
        print("Cette personne a", self.age, "ans")

    def bonjour(self):
        print("Hello")

    def set_modifier_age(self):
        self.age = input("Veuillez renseigner l'âge de la personne: ")
        while not self.age.isnumeric():
            self.age = input("Veuillez renseigner un âge valide: ")
        else:
            return self.age


personne = Personne(14)


class Eleve(Personne):
    def aller_en_cours(self):
        print("Je vais en cours.")

    def affichage_age(self):
        print("J'ai", self.age, "ans.")


eleve = Eleve(14)


class Professor(Personne):
    def __init__(self, matiereenseignee):
        self.__matiereEnseignee = matiereenseignee

    def set_matiereenseignee(self):
        self.__matiereEnseignee = input("Veuillez renseigner la matière enseignée: ")
        while not self.__matiereEnseignee.islower():
            self.__matiereEnseignee = input("Veuillez renseigner une matière valide: ")
        else:
            return self.__matiereEnseignee

    def get_matiereenseignee(self):
        print("Ce professeur enseigne", self.__matiereEnseignee)

    def enseigner(self):
        print("Le cours va commencer.")


professor = Professor("")

eleve.bonjour()
eleve.aller_en_cours()
eleve.set_modifier_age()
eleve.affichage_age()
professor.bonjour()
professor.set_modifier_age()
professor.afficher_age()
professor.enseigner()