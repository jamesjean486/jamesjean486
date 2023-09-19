from abc import ABC , abstractmethod
#from abc import ABCMeta

#class Vehicle(metaclass=ABCMeta):
class Vehicle(ABC):

    def __init__(self, modelo, ano):
        self.model = modelo
        self.year = ano

    @abstractmethod
    def turnOn(self):
        pass
        # print("Put the key in the ignition")
        # print("Turn the key")
        # print("Starting the engine....")
        # print("Start and go!")



    def turnOff(self):
        pass
        # print("put the gear in neutral")
        # print("pull the handbrake")
        # print("urn the key in the opposite direction")
        # print("turn off the engine. . .")


    def show(self):
        print("Model: ", self.model)
        print("Year: ", str(self.year))
