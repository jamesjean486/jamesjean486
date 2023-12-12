from Pessoa import Pessoa

class Jogador(Pessoa):
    def __init__(self, id, nome, numero_camisa, posicao):
        super().__init__(id, nome)
        self.numeroCamisa = numero_camisa
        self.__posicao = posicao
        self.proximo = None
        
#método acessor
    def getJogador(self):
        return f"{super().name},{self.numeroCamisa} ,{self.__posicao}"

    def getnumero(self):
        return self.numeroCamisa
#método modificador
    def setMatricula(self, posicao):
       self.__posicao = posicao

    def setnumero(self , numero):
        self.numeroCamisa = numero

 





        # self.proximo = proximo
        # novo_jogador = nome,numero_camisa
        # if self.inicio is None or self.inicio.numero_camisa > novo_jogador.nome.numero_camisa:
        #     novo_jogador.proximo = self.inicio
        #     self.inicio = novo_jogador
        #     return
        # jogadoratual = self.inicio

        # while jogadoratual.proximo is not None and jogadoratual.proximo.nome.numero_camisa < novo_jogador.jogador.numero_camisa:
        #     jogadoratual = jogadoratual.proximo

        # novo_jogador.proximo = jogadoratual.proximo
        # jogadoratual.proximo = novo_jogador        


    def jogar(self):
         print("Vamos Jogar!!!", self.name)
         print("Na pocição: ", self.__posicao)



    