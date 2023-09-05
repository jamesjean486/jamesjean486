from Categoria import Category
class Vehicle:
     def __init__(self, marca = "Honda", ano = 2014, cat = Category(None)):
        self.id = None
        self.brand = marca
        self.year = ano
        self.category = cat

     def __str__(self):
        txt = "BRAND: " + self.brand + "\n"
        txt += "YEAR: " +  str(self.year) + "\n"
        txt += "CATEGORY: " + str(self.category.name) + "\n"
        return txt

     def printing(self):
        print("Vehicle : >>>  \n", self)
        # print("Vehicle : >>>  \n", self.__str__)
        # print("Vehicle : >>>  \n", str(self))