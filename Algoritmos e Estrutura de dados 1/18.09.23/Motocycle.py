from Veicle import Vehicle

class Motorcycle(Vehicle):

    def __init__(self, modelo, ano, cilindradas):
        super().__init__(modelo, ano)
        self.engineCapacity = cilindradas

    def turnOn(self):
        print("Put on the helmet")
        print("lower the support foot")
        print("Put the key in the ignition")
        print("Turn the key")
        print("Starting the engine....")
        print("Start and go!")

    def show(self):
        super().show()
        print("Engiene Capacity: ", str(self.engineCapacity))