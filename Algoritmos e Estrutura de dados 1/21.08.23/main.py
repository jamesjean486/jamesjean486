from Pessoa import Pessoa
from Cidade import Cidade

c1 = Cidade("POA City", "RS") 

p1 = Pessoa("Jhon", 1.75, c1)
#outra maneira é:

p2 = Pessoa("Mary", 1.80, c1)
p3 = Pessoa("Juan", 1.65, Cidade("Alvorada City", "RS"))

p1.printing()
p3.printing()

print(p2)

print("IMC de ", p1.nome , "= " + str(p1.getIMC(75.640)) )
#outra maneira tb seria:
# print("IMC de ", p1.nome , "= " , p1.getIMC(75.640))