from No import No

class Battery:
    def __init__(self):
        self.topo =  None
        self.tamanho = 0
    
    def add(self,titulo):
        no = No(titulo)
        no.proximo = self.topo
        self.topo = no
        self.tamanho += 1
        self.printing()


    def printing(self):
        if self.topo == None:
            print("Pilha vazia")
        aux = self.topo
        txt = ""
        while(aux):
            txt += aux.dado + " - "
            aux = aux.proximo
        print (txt)
        print("Total: "  , self.tamanho)         
        

    def remover(self):
        if self.topo == None:
            print('Pilha vazia!!!')
        else:
            titulo = self.topo.dado
            self.topo = self.topo.proximo
            self.tamanho -= 1
            return titulo
       