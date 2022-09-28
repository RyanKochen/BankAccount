class BankAccount:
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.int_rate * self.balance)
        else:
            print("invalid")
        return self


ryan = BankAccount(.15, 500)
felix = BankAccount(.2,700)

ryan.deposit(500).deposit(300).deposit(400).withdraw(600).yield_interest().display_account_info()
felix.deposit(300).deposit(200).withdraw(100).withdraw(150).withdraw(60).withdraw(80).yield_interest().display_account_info()




