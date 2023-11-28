from torre import Tower

class Apartemento:

    def __init__(self, numero, torre):
        self.id = None
        self.number = numero 
        self.tower = torre
        self.vaga = None
        self.proximo = None


    def cadastrar(self):
        print("Apartamento Cadastrado!")

    
    def __str__(self):
        text = "\n Number: " + str(self.number)
        text += "\n Vaga: " + str(self.vaga)
        text += "\n Tower: " + self.tower.name
        return text

    def printing(self):
        print( self )

    