class BankAccount:
    def __init__(self, owner, starting_balance):
        # We assign to the PUBLIC names (self.owner, self.balance)
        # This forces the validation logic in the setters to run immediately!
        self.__owner = owner
        self.balance = starting_balance

    # --- OWNER PROPERTY (String Validation) ---
    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Owner name must be a non-empty string.")
        self.__owner = name

    # --- BALANCE PROPERTY (Math Validation) ---
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Balance must be a number.")
        if amount < 0:
            raise ValueError("Insufficient Funds: Balance cannot be negative.")
        self._balance = amount

    # --- METHODS (Using the properties) ---
    def deposit(self, amount):
        if amount <= 0:
            print("--- Deposit failed: Amount must be positive. ---")
            return
        # This triggers the @balance.setter automatically
        self.balance += amount
        print(f"Success! Deposited ${amount}. Current balance: ${self.balance}")

    def withdraw(self, amount):
        try:
            # This triggers the @balance.setter which checks for negatives
            self.balance -= amount
            print(f"Success! Withdrew ${amount}. Remaining: ${self.balance}")
        except ValueError as e:
            print(f"--- Withdrawal failed: {e} ---")


# 1. Create a valid account
acct = BankAccount("Alice", 1000)

# 2. Try to set an invalid name (Should fail)
try:
    acct.owner = ""
except ValueError as e:
    print(f"Validation Error: {e}")

# 3. Try to set a negative balance directly (Should fail)
try:
    acct.balance = -500
except ValueError as e:
    print(f"Validation Error: {e}")

# 4. Use the methods correctly
acct.deposit(500)   # Balance becomes 1500
acct.withdraw(2000) # Should fail because 1500 - 2000 = -500 (Value Error!)