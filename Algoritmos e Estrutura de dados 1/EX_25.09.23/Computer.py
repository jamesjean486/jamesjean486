from abc import ABC, abstractmethod
class Computador(ABC):
    def __init__(self, modelo, cor, preco):
        self.model = modelo
        self.color = cor
        self.price = preco

    def getInformacoes(self):
        return (f"Modelo:  {self.model}, \n Color:  {self.color} \n, Price: R$ {str(self.price)}")

    @abstractmethod
    def cadastrar():
        pass


