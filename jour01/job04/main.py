class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def sepresenter(self):
        return f'{self.nom} {self.prenom}'


personne = Personne('GUARNERA', 'Sébastien')

print("Je suis", personne.sepresenter())

personne = Personne("Jean", "Dupond")

print("Je suis", personne.sepresenter())
