import uuid
class BankAccount:
    def __init__(self,account_type, balance=0,interest_rate=0.1):
        'initialize the bankaccount class'
        self.account_number=str(uuid.uuid4())
        self.account_type=account_type
        self.balance=balance
        self.interest_rate=interest_rate
        self.account_type=account_type
    
    def display_balance(self):
        'returns the user bank account balance'
        return f'{self.balance}'
    
    def deposit(self, amount):
        'deposits money in the user bank account'
        self.balance = self.balance + amount

    def withdraw(self, amount):
        '''withdraw money from user's bank account balance'''
        if amount > self.balance:
            return f'Error. Insufficient funds.You are not eligible to withdraw {amount}.'
        else:
            self.balance=self.balance - amount
            return f'{amount} withdrawn successfully'
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return interest

 







