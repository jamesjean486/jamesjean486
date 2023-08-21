#classe sempre com letra maiuscula, e nome do arquivo  com o msm nome da classe 
class Pessoa:
    #definindo o método construtor
    def __init__(self, name, age):
        #construir os atributos tal como definir seus valores
        #teste 
        print("obj instanciado")
        #atributo + atributo = parâmetro
        self.nome = name
        self.idade = age
        
