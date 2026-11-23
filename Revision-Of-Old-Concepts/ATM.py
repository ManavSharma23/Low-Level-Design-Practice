#Create a class called ATM.

# Requirements:

# 1. The constructor should accept:
#    - Account holder's name
#    - Initial balance
#    - PIN

# 2. Store the balance and PIN as private attributes.

# 3. Implement these methods:

#    - check_balance(pin) – Display the balance if the PIN is correct.
#    - deposit(amount) – Add money to the account.
#    - withdraw(amount, pin) – Withdraw money after PIN verification.
#    - change_pin(old_pin, new_pin) – Change the PIN after verification.

# 4. Prevent negative deposits and withdrawals.

# 5. Do not allow withdrawals greater than the available balance.



class ATM :
    
    def __init__(self,name: str, balance: float ,pin: int):
        self.name=name
        self.__balance=balance
        self.__pin=pin

    def get_pin(self):
        return self.__pin
    
    def get_balance(self):
        return self.__balance

    def check_balance(self,pin):

        if pin == self.get_pin():
            print(self.get_balance())
        else:
            print("Incorrect PIN")

    def deposit_amount(self,amount):
        if amount > 0:
            self.__balance+=amount
            print("Amount Deposited")
        else:
            print("Enter a valid amount")
    
    def withdraw_amount(self,amount,pin):

        if pin == self.get_pin():
            if amount > 0 and amount <= self.get_balance():
                self.__balance-=amount
                print("Amount Withdraw")
            else:
                print("Insufficient money ")
        else:
            print("wrong pin entered")


    def change_pin(self,old_pin,new_pin):
        if old_pin==self.get_pin():
            self.__pin=new_pin
            print("PIN Changed")
        else:
            print("wrong pin entered")        


