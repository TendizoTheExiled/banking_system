from bank_account import BankAccount
account=BankAccount('transfer')
import uuid
from datetime import datetime

class Transaction:
    def __init__(self, amount, transaction_type, status="pending"):
        """
        Initialize a transaction object.
        
        transaction_type: 'deposit', 'withdrawal', 'transfer', 'payment'
        status: 'pending', 'completed', 'canceled'
        """
        self.transaction_id = str(uuid.uuid4())  # unique ID
        self.amount = amount
        self.type = transaction_type
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.status = status

    def execute(self, account):
        """Executes the transaction on the given BankAccount object."""
        if self.status != "pending":
            return f"Transaction {self.transaction_id} already {self.status}."

        if self.type == "deposit":
            account.balance += self.amount
            self.status = "completed"

        elif self.type == "withdrawal":
            if account.balance >= self.amount:
                account.balance -= self.amount
                self.status = "completed"
            else:
                self.status = "failed"
                return f"Insufficient funds for withdrawal."

        # More transaction types (transfer, payment) could be added here

        return f"Transaction {self.transaction_id} executed successfully."

    def cancel(self):
        """Cancels the transaction if still pending."""
        if self.status == "pending":
            self.status = "canceled"
            return f"Transaction {self.transaction_id} canceled."
        return f"Cannot cancel. Transaction is {self.status}."

    def view_receipt(self):
        """Displays a transaction receipt."""
        return (
            f"--- Transaction Receipt ---\n"
            f"ID: {self.transaction_id}\n"
            f"Type: {self.type}\n"
            f"Amount: {self.amount}\n"
            f"Date: {self.date}\n"
            f"Status: {self.status}\n"
            f"---------------------------"  
        )