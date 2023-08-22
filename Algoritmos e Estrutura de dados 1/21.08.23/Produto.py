

class Product():
    def __init__(self, name = None, price = 0.0, cat = Category() ):
        self.id = None
        self.nome = name
        self.preco = price
        self.categoria = cat

    def __str__(self):
        txt = "Product: " + self.nome + "\n"
        txt += "Price: R$ " + str(self.preco) + "\n"
        #txt += "Category: " + self.cat.nome
        txt += self.categoria.__str__()
        return txt