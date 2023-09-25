from Computer import Computador

class Note(Computador):
    def __init__(self, modelo, cor, preco, tempoDeBateria):
        super().__init__(modelo, cor, preco)
        self.__bateryTime = tempoDeBateria

    def getInformacoes(self):
        return f"{super().getInformacoes()}, Tempo de Bateria: {self.__bateryTime}"

    def cadastrar():
        print("Sucesss! Your Machine it's ready to get started!")