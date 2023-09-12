from acount import Count

c1 = Count()

c1.balance = 20.0
#c1.setBalance(2.50)

print(c1.getBalance())
c1.deposit(200.0)
print(c1.balance)
c1.withdrawal(50.0)
print(c1.balance)
