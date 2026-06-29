from models import ExpenseTracker


def create_user(tracker):
    name = input("Enter user name: ")

    if tracker.get_user(name):
        print("User already exists.")
    else:
        tracker.add_user(name)
        print("User created successfully.")


def add_income(tracker):
    name = input("Enter user name: ")

    user = tracker.get_user(name)
    if not user:
        print("User not found.")
        return

    amount = float(input("Enter income amount: "))
    source = input("Enter income source: ")
    date = input("Enter date (DD/MM/YYYY): ")

    tracker.add_income(name, amount, source, date)
    print("Income added successfully.")


def add_expense(tracker):
    name = input("Enter user name: ")

    user = tracker.get_user(name)
    if not user:
        print("User not found.")
        return

    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    date = input("Enter date (DD/MM/YYYY): ")

    tracker.add_expense(name, amount, category, date)
    print("Expense added successfully.")


def view_expenses(tracker):
    name = input("Enter user name: ")

    user = tracker.get_user(name)
    if not user:
        print("User not found.")
        return

    if not user.expenses:
        print("No expenses found.")
        return

    print("\nExpenses:")
    user.view_expenses()


def calculate_savings(tracker):
    name = input("Enter user name: ")

    user = tracker.get_user(name)
    if not user:
        print("User not found.")
        return

    savings = user.calculate_savings()
    print(f"Current savings: {savings}")


def display_menu():
    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Create User")
    print("2. Add Income")
    print("3. Add Expense")
    print("4. View Expenses")
    print("5. Calculate Savings")
    print("6. Save Data")
    print("7. Exit")