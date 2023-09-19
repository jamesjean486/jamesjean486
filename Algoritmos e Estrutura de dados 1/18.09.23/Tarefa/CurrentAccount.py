from BankAccount import BankAccnt

class CurrentA(BankAccnt):

    def __init__(self, agencia, numerodaconta, senha, taxa_manutencao):
        super().__init__(agencia, numerodaconta,senha)
        self.maintenancefee = taxa_manutencao
        
    
    def deposit(self, valor):
        self.balance += valor
        print("Balance Value: R$  " , self.balance)

    def show(self):
        super().show()
        print("Maintenance fee: R$ ", str(self.maintenancefee))

