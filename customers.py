from bank_account import BankAccount

class Customer:

    def __init__(self, fname, sname,age, id_number,email,phone):
        'initialize customer class. '
        self.age=age
        self.fname=fname
        self.sname=sname
        self.id_number=id_number
        self.email=email
        self.phone=phone
        self.accounts=[] #takes in list of BankAcount Objects

    def display_age(self):
        'displays customer age'
        return f'{self.age}'    

    def display_names(self):
        'displays the customer full name'
        return f'{self.fname} {self.sname}'    

    def view_profile(self, account):
        'displays customers details '
        return (
        f"ID Number: {self.id_number} \n"
        f"Name: {self.display_names()} \n"
        f"Age: {self.display_age()}\n"
        f"Current Balance: {account.display_balance()}\n"
        f"Email Address: {self.email}\n"
        f"Phone: {self.phone}"
        
        )
    def open_account(self,account):
        'openning a bank Account (e.g Savings)'
        self.accounts.append(account) #adds account to list of accounts
        

    def close_account(self, account): 
        'closing an account'
        self.accounts.remove(account) #removes BankAcount object from the list

    def my_accounts(self): 
        'returns a BankAcount Object from a list'
        for account in self.accounts:
            return account

    def request_loan(self):
        pass
    
    def view_accounts(self):
        return [acc.display_balance() for acc in self.accounts]