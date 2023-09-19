from BankAccount import BankAccnt

class SavingsA(BankAccnt):

    def __init__(self, agencia, numerodaconta, senha, taxa_rendimento):
        super().__init__(agencia, numerodaconta,senha)
        self.yieldrate = taxa_rendimento
        
    
    def deposit(self, valor):
        self.balance += valor
        print("Balance Value: R$  " , self.balance)

    def show(self):
        super().show()
        print("Yield Rate: R$ ", str(self.yieldrate))

