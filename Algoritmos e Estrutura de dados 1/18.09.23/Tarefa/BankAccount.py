from abc import ABC , abstractmethod
#from abc import ABCMeta
class BankAccnt(ABC):

    def __init__(self,agencia, numerodaconta, senha):
        self.agency = agencia 
        self.balance =  0.0
        self.accountNumber = numerodaconta
        self.password = senha

    @abstractmethod
    def deposit(self, valor):
        pass
    
    def verificar_senha(self, senha_informada):
        if senha_informada == self.password:
            print("Authenticating data...\n")
            print("Accessing account...\n")
            print("Sucess! You also acess your Account")
            return True
        else:
            print("Wrong Password! Try Again!, more 2 attempts")
            return False

    def show(self):
        print("Agency: ", self.agency)
        print("Number Account: ", str(self.accountNumber))
        print("Current Balance: ", self.balace)
    
