from Veiculo import Vehicle
from Categoria import Category
from Carro import Car
from Moto import Motorbike

cat01 = Category("Sedan")
cat02 = Category("SUV")
cat03 = Category("Sport")

v1 = Vehicle()
v1.printing()

car01 = Car("BMW", 2021, cat02, 4)
car01.printing()

motorbike01 = Motorbike("Harley davison", 1970, cat03, 353)
motorbike01.printing()