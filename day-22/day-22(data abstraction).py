
#in abstract class we cant create an obj for the parent
from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    def current_balance(self):
        print("You can check your balance")
    def view_histroy(self):
        print("You can check your balance")

class SavingAccount(BankAccount):
    def deposit(self):
        print("upto 10L per annum")
    def withdraw(self):
        print("Maintain minimum balance")

class Current_Balance(BankAccount):
    def deposit(self):
        print("Unlimited transactions")
    def withdraw(self):
        print("Unlimited withdraws")

class Joint_Account(BankAccount):
    def deposit(self):
        print("Any holder can deposit")
    def withdraw(self):
        print("Joint or either can deposit")

class StudentAccount(BankAccount):
    def deposit(self):
        print("small deposit")
    def withdraw(self):
        print("Limited")

class ODAccount(BankAccount):
    def deposit(self):
        print("Deposit to repay loan")
    def withdraw(self):
        print("Can withdraw more than balance")

class SalaryAccount(BankAccount):
    def deposit(self):
        print("Salary credited + extra deposits allowed")
    def withdraw(self):
        print("Easy withdrawals like savings")

anju = SavingAccount()
print("------------------------Anju-----------------------")
anju.deposit()
anju.withdraw()
anju.current_balance()
anju.view_histroy()


hima = Current_Balance()
print("------------------------Hima-----------------------")
hima.deposit()
hima.withdraw()
hima.current_balance()
hima.view_histroy()

keerthi = Joint_Account()
print("----------------------Keerthi-----------------------")
keerthi.deposit()
keerthi.withdraw()
keerthi.current_balance()
keerthi.view_histroy()

prasanna = StudentAccount()
print("----------------------Prasanna-----------------------")
prasanna.deposit()
prasanna.withdraw()
prasanna.current_balance()
prasanna.view_histroy()

deeksha = ODAccount()
print("----------------------Deeksha-----------------------")
deeksha.deposit()
deeksha.withdraw()
deeksha.current_balance()
deeksha.view_histroy()

suma = SalaryAccount()
print("----------------------Suma-----------------------")
suma.deposit()
suma.withdraw()
suma.current_balance()
suma.view_histroy()
    

        


    


    
