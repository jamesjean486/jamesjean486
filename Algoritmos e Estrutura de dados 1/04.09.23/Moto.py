from Veiculo import Vehicle
class Motorbike(Vehicle):
    def __init__(self, marca, ano, cat, cilindradas ):
        super().__init__(marca, ano, cat)
        self.displacement = cilindradas
    def __str__(self):
        txt = super().__str__()
        txt += "Displacement :" + str(self.displacement)
        return txt
    def printing(self):
        print("Motocycle >>>>  \n" , self)