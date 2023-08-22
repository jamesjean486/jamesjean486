from Cidade import Cidade

class Pessoa:
    def __init__(self, name = None, heigth = 0.0, city = Cidade()):
        self.id = None
        self.nome = name
        self.altura = heigth
        self.cidade = city
      
    def __str__(self):
        txt = "Name: " + self.nome + "\n"
        txt += "Heigth: " + str(self.altura) + "\n"
        txt += "City: " + self.cidade.nome + "\n"
        txt += "State: " + self.cidade.uf + "\n"
        return txt




    def printing(self):
        print("Name: ", self.nome)
        print("Heigth: " , self.altura)
        self.cidade.printing()

    def getIMC(self, weigth ):
        return weigth / (self.altura * self.altura)