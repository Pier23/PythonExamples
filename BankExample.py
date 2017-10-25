''' This is proposed as a semplificate example of Object oriented programming in python'''

#Definition of super class who define the properties of an account
class Account:
#Class Initialization
    def __init__(self, name, accountNumber):
        self.name = name
        self.accountNumber = accountNumber

#Definition of class who implement the super class
class BankAccount(Account):
#Class Initialization
    def __init__(self, name,accountNumber,amount):
        super().__init__(name, accountNumber)
        self.__balance = amount

#method that allow to withdraw the money
    def withdraw(self, amount):
        self.__balance -= amount

#Method that allow to deposit money
    def deposit(self, amount):
        self.__balance += amount

#Method that stamp a description
    def description(self):
        print('Name: ' + self.name,
        'Account: ' + self.accountNumber,
        'Balance: ' + str(self.__balance))

#Getter and setter
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        self.withdraw(self.__balance)
        self.deposit(amount)

#Class that allow to do some bank operation
class BankAccountManager:
    @staticmethod
    def bankTransfer(source, recipient, amount):
        source.withdraw(amount)
        recipient.deposit(amount)

#Test
b1 = BankAccount('Pippo', '08990', 1000)
b2 = BankAccount('Pino', '07790', 2000)

b1.description()
b2.description()

BankAccountManager.bankTransfer(b1,b2, 500)

b1.description()
b2.description()
