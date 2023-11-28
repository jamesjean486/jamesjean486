class Tower:

    def __init__(self, nome, end):
        self.id = None
        self.name = nome 
        self.address = end

    def cadastrar(self):
        print("Torre Cadastrada!")

    
    def __str__(self):
        text = "\n Name: " + self.name
        text += "\n Address: " + self.address
        return text

    def printing(self):
        print( self )