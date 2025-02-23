from expense import Expense

class ExpenseDatabase:
    def __init__(self):
        """
        Initializes an ExpenseDatabase instance to store expenses.
        """
        self.expenses = []

    def add_expense(self, expense: Expense):
        """
        Adds an Expense instance to the database.
        
        :param expense: The Expense instance to add.
        """
        self.expenses.append(expense)

    def remove_expense(self, expense_id: str):
        """
        Removes an expense by its ID.

        :param expense_id: The ID of the expense to remove.
        """
        self.expenses = [exp for exp in self.expenses if exp.id != expense_id]

    def get_expense_by_id(self, expense_id: str):
        """
        Retrieves an expense by its ID.

        :param expense_id: The ID of the expense.
        :return: The Expense instance or None if not found.
        """
        return next((exp for exp in self.expenses if exp.id == expense_id), None)

    def get_expense_by_title(self, expense_title: str):
        """
        Retrieves all expenses with a given title.

        :param expense_title: The title of the expense.
        :return: List of Expense instances with the given title.
        """
        return [exp for exp in self.expenses if exp.title.lower() == expense_title.lower()]

    def to_dict(self):
        """
        Converts the database to a list of dictionaries representing expenses.
        
        :return: List of dictionaries.
        """
        return [expense.to_dict() for expense in self.expenses]