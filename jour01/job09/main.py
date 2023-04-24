class Student:
    def __init__(self, nom, prenom, numero, credit):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero = numero
        self.__credit = credit

    def add_credit(self):
        self.__credit += 10
        while not self.__credit > 0:
            self.__credit += 10
        else:
            return self.__credit

    def get_credit(self):
        print("Le nombre de crédits de", self.__prenom, self.__nom, "est de", self.__credit, "points.")

    def studenteval(self):
        if self.__credit >= 90:
            print("Excellent")
        elif 80 <= self.__credit <= 90:
            print("Très bien")
        elif 70 <= self.__credit <= 80:
            print("Bien")
        elif 60 <= self.__credit <= 70:
            print("Passable")
        else:
            print("Insuffisant")




student = Student("Doe", "John", 145, 0)

student.add_credit()
student.add_credit()
student.add_credit()
student.get_credit()
student.studenteval()
