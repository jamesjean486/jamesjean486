class Count:
    fee = 1.99
    logged = True

    def __init__(self):
        self.__balance = 0.0

    def getBalance(self):
        if self.logged:
            return self.__balance
        else:
            print("You don't have permission acess!!")
            return None


    def setBalance(self, value):
        if self.logged and value >= 0:
            self.__balance = value
        else:
            print("You don't have permission or invalid value reported!!")

    @property
    def balance(self):
         if self.logged:
            return self.__balance
         else:
            print("You don't have permission acess!!")
            return None

    @balance.setter
    def balance(self,value):
        if self.logged and value >= 0:
            self.__balance = value
        else:
            print("You don't have permission or invalid value reported!!")

    def __discountFee(self):
        self.__balance -= self.fee

    def withdrawal(self,value):
        if self.__balance + value >= self.fee:
            self.__balance += value
            self.__discountFee()
        else:
            print(" ! ! ! Insufficient Value ! ! !")

    def deposit(self,value):
        if self.__balance - value >= self.fee:
            self.__balance -= value
            self.__discountFee()
        else:
            print(" ! ! ! Insufficient Balance ! ! !")

