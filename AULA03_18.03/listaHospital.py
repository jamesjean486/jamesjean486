""""A lista deve ser ordenada pelo número do prontuário."""
from no import No
class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
    
    def addInicio(self,nome:str, idade:int, prontuario:int):
        if prontuario is None:
            print( "Prontuário não existe na lista!")
        if  prontuario ==  self.inicio.prontuario_paciente:
            print("Prontuário já existe na lista!")

        no = No(nome, idade, prontuario)
        
        if self.inicio == None:
            self.inicio = no
            self.fim = no 
        else:
            no.proximo = self.primeiro
            self.primeiro = no
            self.tamanho += 1
            self.imprimir()


    def imprimir(self):
        print("---------------------")
        if self.inicio == None:
            print("Lista Vazia!")
        else:
            aux = self.inicio
            texto = ""
            while( aux ):
                texto += str(aux.nome) + ": "
                texto += str(aux.idade) + ":  "
                texto += aux.prontuario 
                aux = aux.proximo
                print( texto )
            



    







    