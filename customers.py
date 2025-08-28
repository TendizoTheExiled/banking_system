from .bank_account import BankAccount
b_a=BankAccount()
class Customer:

    def __init__(self, fname, sname,age, id_number,email,phone):
        'initialize customer class. '
        self.age=age
        self.fname=fname
        self.sname=sname
        self.id_number=id_number
        self.email=email
        self.phone=phone
        self.accounts=[]

    def display_age(self):
        'displays customer age'
        return f'{self.age}'    

    def display_names(self):
        'displays the customer full name'
        return f'{self.fname} {self.sname}'    

    def view_profile(self, account):
        'displays customers details '
        return (
        f"{self.id_number} \n"
        f"{self.display_names()} \n"
        f"{self.display_age()}\n"
        f"{account.display_balance()}"
        f"{self.email}"
        f"{self.phone}"
        
        )
    def open_account(self,account):
        self.accounts.append(account) #adds account to list of accounts
        

    def close_account(self, account):
        self.accounts.remove(account)

    def request_loan(self):
        pass
