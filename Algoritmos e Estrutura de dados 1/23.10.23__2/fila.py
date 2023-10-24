from No import No

class Fila:
    def __init__(self):
        self.inicio =  None
        self.fim =  None
        self.tamanho = 0
    
    def add(self,valor):
        no = No(valor)
        if self.inicio == None:
            self.inicio = no
        else:
            self.fim.proximo = no
        self.fim = no
        self.tamanho += 1
        self.printing()


    def printing(self):
        if self.inicio == None:
            print("Fila vazia")
        aux = self.inicio
        txt = ""
        while(aux):
            txt += str( aux.dado) + " - "
            aux = aux.proximo
        print (txt)
        print("Total: "  , self.tamanho)         
        

    def remover(self):
        if self.inicio == None:
            print('Fila vazia!!!')
        elif self.inicio.proximo == None :
            self.fim = None
        self.inicio = self.inicio.proximo
        self.tamanho -= 1
        self.printing()
