from Veiculo import Vehicle
class Car(Vehicle):
    def __init__(self, marca, ano, cat, qtdportas ):
        super().__init__(marca, ano, cat)
        self.doorsnumber = qtdportas 
    def __str__(self):
        txt = super().__str__()
        txt += "Number of Doors: " + str(self.doorsnumber)
        return txt

    def printing(self):
        super().printing()
        print("Number of Doors >>>> " + str(self.doorsnumber))