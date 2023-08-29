class Person:
    def __init__(self, nome = "Daniel", telefone = "(51)999999999"):
        self.name = nome
        self.phone = telefone

    def __str__(self):
        txt = "Name: " + self.name + "\n"
        txt += "Fone: " + self.phone + "\n"
        return txt
    def printing(self):
        print(self)