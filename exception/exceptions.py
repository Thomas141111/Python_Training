class AccountAlreadyExistsError(Exception):
    def __init__(self, account_number):
        super().__init__(f"Account with number {account_number} already exists.")
        self.account_number = account_number

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Insufficient funds: Current balance is {balance}, attempted withdrawal is {amount}.")
        self.balance = balance
        self.amount = amount