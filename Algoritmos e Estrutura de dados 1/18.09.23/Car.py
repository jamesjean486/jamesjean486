from Veicle import Vehicle

class Car(Vehicle):

    def __init__(self, modelo, ano, nPortas):
        super().__init__(modelo, ano)
        self.doorsnumber = nPortas

    def turnOn(self):
        print("Put on your seat belt")
        print("Adjust the mirrors")
        print("Put the key in the ignition")
        print("Turn the key")
        print("Starting the engine....")
        print("Start and go!")

    def show(self):
        super().show()
        print("Number of doors: ", str(self.doorsnumber))