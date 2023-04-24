class Operation:
    def __init__(self, n1, n2):
        self.nombre1 = n1
        self.nombre2 = n2

    def premier(self):
        print("Le nombre1 est", self.nombre1)

    def deuxieme(self):
        print("Le nombre2 est", self.nombre2)


operation = Operation(12, 3)

operation.premier()
operation.deuxieme()
