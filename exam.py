import uuid
from datetime import datetime

class Expense:
    def __init__(self, title, amount):
        self.id = str(uuid.uuid4())  # Unique ID for each expense
        self.title = title          # Title of the expense
        self.amount = amount        # Amount of the expense
        self.created_at = datetime.utcnow()  # Timestamp when the expense is created
        self.updated_at = self.created_at    # Timestamp for the last update

    def update(self, title=None, amount=None):
        
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class ExpenseDatabase:
    def __init__(self):
        self.expenses = []  # List to store Expense instances

    def add_expense(self, title, amount):

        expense = Expense(title, amount)
        self.expenses.append(expense)
        return expense

    def remove_expense(self, expense_id):
       
        self.expenses = [expense for expense in self.expenses if expense.id != expense_id]

    def get_expense_by_id(self, expense_id):
        
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None

    def get_expense_by_title(self, title):
     
        return [expense for expense in self.expenses if expense.title == title]

    def to_dict(self):
        
        return [expense.to_dict() for expense in self.expenses]