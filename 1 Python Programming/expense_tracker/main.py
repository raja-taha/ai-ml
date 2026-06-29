from models import ExpenseTracker
from operations import (
    create_user,
    add_income,
    add_expense,
    view_expenses,
    calculate_savings,
    display_menu
)


def main():
    tracker = ExpenseTracker()

    tracker.load_data()

    while True:
        display_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            create_user(tracker)

        elif choice == "2":
            add_income(tracker)

        elif choice == "3":
            add_expense(tracker)

        elif choice == "4":
            view_expenses(tracker)

        elif choice == "5":
            calculate_savings(tracker)

        elif choice == "6":
            tracker.save_data()
            print("Data saved successfully.")

        elif choice == "7":
            tracker.save_data()
            print("Data saved.")
            print("Exiting program...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()