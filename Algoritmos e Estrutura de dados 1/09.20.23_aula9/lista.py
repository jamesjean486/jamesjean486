from no import No

class Lista:

    def __init__(self):
        self.primeiro = None
        self.tamanho = 0
    
    def addInicio(self,valor):
        no = No(valor)
        if self.primeiro == None:
            self.primeiro = no

        else:
            no.proximo = self.primeiro
            self.primeiro = no
        self.tamanho += 1
        self.imprimir()


    def imprimir(self):
        aux = self.primeiro
        while(aux):
            print(aux.dado)
            aux = aux.proximo
        print("Total: "  , self.tamanho) 


    def addNoFim(self,valor):
        no = No(valor)
        if self.primeiro == None:
            self.primeiro = no
            self.tamanho += 1
        else:
             aux = self.primeiro
             while(aux):
                if aux.proximo == None:
                    aux.proximo = no
                    break


    # def addNoFim(self,valor):
    #     no = No(valor)
    #     if self.primeiro != None:
    #         aux = self.primeiro
    #         while aux.proximo:
    #             aux = aux.proximo
    #         aux.proximo = no
    #     else:
    #         self.primeiro = no
    #     self.tamanho += 1
    #     self.imprimir()

    def removedoInicio(self):
        if self.primeiro == None:
            print('lista vazia!!!')
        elif self.primeiro.proximo == None :
            self.primeiro = None
            self.tamanho = 0
        else:
            self.primeiro = self.primeiro.proximo
            self.tamanho -= 1
        self.imprimir()




# def removedoInicio(self):
#         if self.primeiro == None:
#             print('lista vazia!!!')
#         else:
#             self.primeiro = self.primeiro.proximo
#             self.tamanho -= 1
#         self.imprimir()


    def removedoFim(self):
        if self.primeiro == None:
            print('lista vazia!!!')
        elif self.primeiro.proximo == None:
            self.primeiroc = None
            self.tamanho -= 1
        else:
            anterior = self.primeiro
            aux = self.primeiro.proximo
            while aux.proximo:
                anterior = aux
                aux = aux.proximo
            anterior.proximo = None
            self.tamanho -= 1
        self.imprimir()
