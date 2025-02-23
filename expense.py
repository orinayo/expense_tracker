import uuid
from datetime import datetime, timezone

class Expense:
    def __init__(self, title: str, amount: float):
        """
        Initializes an Expense instance.
        
        :param title: Title of the expense.
        :param amount: Amount of the expense.
        """
        self.id = str(uuid.uuid4())  # Unique identifier as a UUID string
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)
        self.updated_at = self.created_at  # Initially set to created_at

    def update(self, title: str = None, amount: float = None):
        """
        Updates the expense details.

        :param title: New title (if provided).
        :param amount: New amount (if provided).
        """
        if not title and not amount:
            return
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc)

    def to_dict(self):
        """
        Converts the Expense instance to a dictionary.
        :return: Dictionary representation of the Expense.
        """
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
