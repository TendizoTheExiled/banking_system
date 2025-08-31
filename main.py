from bank_account import BankAccount
from customers import Customer
from transactions import Transaction
acc1=BankAccount('M123k','savings',34999)
#print(acc1.display_balance())

customer1=Customer('Tendai','Kamwathendo',24,'CU3456l','tendaikamwathendo@gmail.com','0997500320')
customer1.open_account(acc1)
t1=Transaction(4000,'deposit')
print(t1.view_receipt())
#print(customer1.view_profile(acc1))
#print(customer1.my_accounts().account_type)

#acc1.apply_interest()
#print(customer1.view_accounts())
