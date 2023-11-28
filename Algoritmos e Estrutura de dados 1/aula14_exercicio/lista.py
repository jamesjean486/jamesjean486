from apartamento import Apartemento

class Lista:

    def __init__(self):
        self.primeiro = None
        self.tamanho = 0
    
    def add(self,ap):
        if self.primeiro == None:
            self.primeiro = ap

        else:
            ant = self.primeiro
            aux = self.primeiro.proximo
            while aux != None:
                if ap.vaga < aux.vaga:
                    ap.proximo = ant.proximo
                    ant.proximo = ap
                    break
                else:
                    ant = aux
                    aux = aux.proximo
            if aux == None and ap.vaga >= ant.vaga:
                ant.proximno = ap


    def imprimir(self):
        print("---------------------")
        if self.inicio == None:
            print("Lista Vazia!")
        else:
            aux = self.inicio
            while aux :
                print( aux )
                aux = aux.proximo
            print( "Tamanho: ", str(self.tamanho))


def remover(self,ap):
        tamAtual = self.tamanho
        if self.inicio == None:
            print("Lista Vazia")
            
        elif self.inicio.proximo == None and self.inicio.dado == ap:
            self.inicio = None
            self.tamanho = 0
        else:
            # Lista contendo vários elementos e o valor é igual ao primeiro
            if self.inicio.dado == ap:
                self.inicio = self.inicio.proximo
                self.tamanho -= 1
            # Lista com vários elementos e o valor não está no primeiro    
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux :
                    if aux:
                        ant.proximo = aux.proximo
                        self.tamanho -= 1
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
        if tamAtual == self.tamanho:
            print("Valor não encontrado")
        self.imprimir()