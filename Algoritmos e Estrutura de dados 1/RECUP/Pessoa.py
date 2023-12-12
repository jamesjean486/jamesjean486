from abc import ABC, abstractmethod
class Pessoa():
    def __init__(self, id, nome):
        self.id = id
        self.name = nome
    
    @abstractmethod
    def jogar(self):
       pass

    def imprimir(self):
        print("Nome: " ,self.name)
