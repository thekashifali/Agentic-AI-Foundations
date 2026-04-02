class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name    
        self.balance = balance  

    # Method to deposit money
    def deposit(self, amount):
        if amount>0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Add postive number..")
    # Method to withdraw money
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    # Method to show account details
    def show_details(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.balance}")

p1=BankAccount("Kashif Ali",400)
p2=BankAccount("Hadi",5000)
p1.show_details()
p2.show_details()
p1.deposit(-400)
p1.show_details()