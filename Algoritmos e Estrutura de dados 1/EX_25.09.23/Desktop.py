from Computer import Computador
class Desktop(Computador):
    def __init__(self, modelo, cor, preco, potenciaDaFonte):
        super().__init__(modelo,cor,preco)
        self._sourcePower = potenciaDaFonte

    def getInformacoes(self):
        return f"{super().getInformacoes()}, \n Source Power:{self._sourcePower}"


    def cadastrar():
        print("Sucesss! Your Machine it's ready to get started!")
        