# Expense Tracker

## Project Description

This project is a simple **Expense Tracker** built using Python. It provides:

- An `Expense` class for handling individual expenses.
- An `ExpenseDatabase` class to manage multiple expenses.

The project follows **object-oriented programming (OOP)** principles ensuring modularity.

---

## Cloning the Project

To clone this project, ensure you have **Git installed**, then run:

```sh
git clone git@github.com:orinayo/expense_tracker.git

cd expense-tracker
```

---

## Running the Code

### **Requirements**

This project runs on at least **Python 3.7+**. Ensure Python is installed by checking:

```sh
python --version
```

### **Running the Expense Tracker**

1. Open a terminal and navigate to the project directory.

2. Run a Python interactive shell:

    ```sh
    python
    ```

3. Import the classes:

    ```python
    from expense import Expense
    ```

    ```python
    from expense_database import ExpenseDatabase
    ```

4. Create an **ExpenseDatabase** instance:

    ```python
    db = ExpenseDatabase()
    ```

5. Add an expense:

    ```python
    expense = Expense("Lunch", 15000.0)
    ```

    ```python
    print(expense.to_dict())
    ```

    ```python
    db.add_expense(expense)
    ```

    ```python
    another_expense = Expense("Transportation", 10000.0)
    ```

    ```python
    print(another_expense.to_dict())
    ```

    ```python
    db.add_expense(another_expense)
    ```

6. List all expenses:

    ```python
    print(db.to_dict())
    ```

7. Retrieve an expense by ID:

    ```python
    retrieved_expense = db.get_expense_by_id(expense.id)
    ```

    ```python
    print(retrieved_expense.to_dict() if retrieved_expense else "Expense not found")
    ```

8. Retrieve expense by title:

    ```python
    retrieved_expenses = db.get_expense_by_title(expense.title)
    ```

    ```python
    print([exp.to_dict() for exp in retrieved_expenses])
    ```

9. Update an expense:

    ```python
    retrieved_expense = db.get_expense_by_id(expense.id)
    ```

    ```python
    retrieved_expense.update(amount=30000.0)
    ```

    ```python
    print(retrieved_expense.to_dict())
    ```

    ```python
    print(db.to_dict())
    ```

10. Remove an expense:

    ```python
    db.remove_expense(expense.id)
    ```

    ```python
    print(db.to_dict())
    ```
