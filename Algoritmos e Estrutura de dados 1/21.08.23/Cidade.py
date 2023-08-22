class Cidade:
    def __init__(self, name = None, state = None):
        self.id = None
        self.nome = name
        self.uf = state

    def printing(self):
        print("City name: ", self.nome)
        print("State: ", self.uf)    
    

    
        