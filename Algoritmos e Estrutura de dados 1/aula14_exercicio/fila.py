from apartamento import Apartemento

class Fila:
    def __init__(self):
        self.inicio =  None
        self.fim =  None
        self.tamanho = 0
    
    def add(self,ap):
        if self.inicio == None:
            self.inicio = ap
        else:
            self.fim.proximo = ap
        self.fim = ap
        self.tamanho += 1
        self.printing()


    def printing(self):
        if self.inicio == None:
            print("Fila vazia")
        aux = self.inicio
        txt = ""
        while(aux):
            txt += str( aux.number) +": " 
            txt += aux.tower.name + " - "
            aux = aux.proximo
        print (txt)
        print("Total: "  , self.tamanho)         
        

    def remover(self, numeroVaga):
        if self.inicio == None:
            print('Fila vazia!!!')
        elif self.inicio.proximo == None :
            self.fim = None
        self.inicio.vaga = numeroVaga
        ap = self.inicio
        ap.proximo = None
        self.inicio = self.inicio.proximo
        self.tamanho -= 1
        self.printing()
        return ap
