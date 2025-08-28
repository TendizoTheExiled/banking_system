class BankAccount:
    def __init__(self,account_number,account_type, balance=0,interest_rate=0.25):
        'initialize the bankaccount class'
        self.account_number=account_number
        self.account_type=account_type
        self.balance=balance
        self.interest_rate=interest_rate
        self.type=type
    
    def display_balance(self):
        'returns the user bank account balance'
        return f'Your account Balance is {self.balance}. Thank you for choosing us.'
    
    def deposit(self, amount):
        'deposits money in the user bank account'
        self.balance = self.balance + amount

    def withdraw(self, amount):
        'withdraw money from user bank account balance'
        if amount > self.balance:
            return f'Error. Insufficient funds.You are not eligible to withdraw {amount}.'
        else:
            self.balance=self.balance - amount
            return f'{amount} withdraw was successful'


 







