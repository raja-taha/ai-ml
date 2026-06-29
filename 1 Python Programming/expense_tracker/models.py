

import json


class Expense:
    def __init__(self, amount, category, date):
        self.amount = amount
        self.category = category
        self.date = date

    def expense_details(self):
        return f"Amount: {self.amount}, Category: {self.category}, Date: {self.date}"
    
    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }

class Income:
    def __init__(self, amount, source, date):
        self.amount = amount
        self.source = source
        self.date = date

    def income_details(self):
        return f"Amount: {self.amount}, Source: {self.source}, Date: {self.date}"
    
    def to_dict(self):
        return {
            "amount": self.amount,
            "source": self.source,
            "date": self.date
        }
    
class User:
    def __init__(self, name):
        self.name = name
        self.income = []
        self.expenses = []

    def add_expense(self, amount, category, date):
        expense = Expense(amount, category, date)
        self.expenses.append(expense)

    def view_expenses(self):
        for expense in self.expenses:
            print(f"Amount: {expense.amount}, category: {expense.category}, date: {expense.date}")

    def add_income(self, amount, source, date):
        income = Income(amount, source, date)
        self.income.append(income)

    def calculate_savings(self):
        total_income = sum(income.amount for income in self.income)
        total_expenses = sum(expense.amount for expense in self.expenses)
        savings = total_income - total_expenses
        return savings
    
    def to_dict(self):
        return {
            "name": self.name,
            "income": [income.to_dict() for income in self.income],
            "expenses": [expense.to_dict() for expense in self.expenses]
        }

class ExpenseTracker:
    def __init__(self):
        self.users = {}

    def add_user(self, name):
        if name not in self.users:
            user = User(name)
            self.users[name] = user

    def get_user(self, name):
        return self.users.get(name)
    
    def add_expense(self, user_name, amount, category, date):
        user = self.get_user(user_name)
        if user:
            user.add_expense(amount, category, date)
        else:
            print(f"User {user_name} not found.")

    def add_income(self, user_name, amount, source, date):
        user = self.get_user(user_name)
        if user:
            user.add_income(amount, source, date)
        else:
            print(f"User {user_name} not found.")

    def save_data(self):
        data = {}

        for name, user in self.users.items():
            data[name] = user.to_dict()

        with open("data/expenses.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        try:
            with open("data/expenses.json", "r") as file:
                data = json.load(file)

            for user_name, user_data in data.items():

                user = User(user_data["name"])

                for income_data in user_data["income"]:
                    income = Income(
                        income_data["amount"],
                        income_data["source"],
                        income_data["date"]
                    )
                    user.income.append(income)

                for expense_data in user_data["expenses"]:
                    expense = Expense(
                        expense_data["amount"],
                        expense_data["category"],
                        expense_data["date"]
                    )
                    user.expenses.append(expense)

                self.users[user_name] = user

            print("Data loaded successfully.")

        except FileNotFoundError:
            print("No saved data found.")