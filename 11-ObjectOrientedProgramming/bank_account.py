class Account:
    balance = 0

    def __init__(self, account_id):
        self.account_id = account_id

    def deposit(self, amount):
        balance += amount

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"Withdraw: {amount}")
        else:
            print("Not suffiecient funds")
