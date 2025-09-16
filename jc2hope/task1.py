class BankAccount:
    
    def __init__(self, pAccountNumber, pBalance):
        self.__AccountNumber = pAccountNumber
        self.__Balance = pBalance
        
    def deposit(self,amount):
        self.__Balance = amount + self.__Balance
        
    def withdraw(self,amount):
        self.__Balance = self.__Balance - amount
        
    def getBalance(self):
        return self.__Balance
        
    def getAccountNumber(self):
        return self.__AccountNumber
    
    def setBalance(self,amount):
        self.__Balance = amount
        
    def setAccountNumber(self,number):
        self.__AccountNumber = number
        

bankArr = []

bank1 = BankAccount("34", 400)
bank2 = BankAccount("45", 300)
bank3 = BankAccount("10", 500)

bankArr.append(bank1)
bankArr.append(bank2)
bankArr.append(bank3)

for bank in bankArr:
    print(bank.getBalance())
    bank.deposit(500)
    print(bank.getBalance())
    bank.withdraw(200)
    print(bank.getBalance())
    print()
    
    
print()
bank1.setAccountNumber("50")
print(bank1.getAccountNumber())

print()
bank1.setBalance("1000")
print(bank1.getBalance())
