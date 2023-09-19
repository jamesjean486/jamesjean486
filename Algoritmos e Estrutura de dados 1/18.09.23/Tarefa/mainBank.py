from Savings import SavingsA
from CurrentAccount import CurrentA

currentA1 = CurrentA(8532, 999541225, 74121, 20.00)
currentA1.deposit(50)
ps = input("Digite sua senha: ")
if currentA1.verificar_senha(ps):
    currentA1.show()


saving1 = SavingsA(8532, 9998888225, 74121, 45.00)
saving1.deposit(100)
ps = input("Digite sua senha: ")
if saving1.verificar_senha(ps):
    saving1.show() 