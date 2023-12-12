from Jogadores import Jogador
class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def add(self,jogador):
        if self.inicio == None:
            self.inicio = jogador
        else:
            if jogador.numero_camisa < self.inicio.numero_camisa:
                Jogador.proximo = self.inicio
                self.inicio = jogador
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux != None :
                    if nodo.dado < aux.dado:
                        nodo.proximo = ant.proximo   
                        ant.proximo = nodo
                        #aux = nodo.proximo
                        break
                    else: 
                        ant = aux
                        aux = aux.proximo
                if aux == None and nodo.dado >= ant.dado:
                    ant.proximo = nodo
                    
        self.tamanho += 1
        self.imprimir()