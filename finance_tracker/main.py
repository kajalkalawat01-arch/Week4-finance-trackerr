from datetime import date
from .expense import Expense
from .expense_manager import ExpenseManager
from .budget import Budget
from .report import ExpenseReport


def main():
    manager = ExpenseManager()

    print("=== Personal Finance Tracker ===")

    try:
        monthly_budget = float(input("Enter your monthly budget (Rs.): "))
        budget = Budget(monthly_budget)

        while True:
            print("\n1. Add Expense")
            print("2. View Expenses")
            print("3. Show Total")
            print("4. Search Expenses")
            print("5. Export CSV Report")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                expense_date = input(
                    "Date (YYYY-MM-DD, blank for today): "
                ).strip()
                if not expense_date:
                    expense_date = date.today().isoformat()

                amount = input("Amount (Rs.): ")
                category = input(
                    "Category (Food, Travel, Shopping, Education, "
                    "Bills, Health, Other): "
                ).strip().title()
                description = input("Description: ").strip()

                Expense.validate(
                    expense_date, amount, category, description
                )
                manager.add_expense(
                    Expense(expense_date, amount, category, description)
                )
                print("Expense added successfully!")

            elif choice == "2":
                if not manager.expenses:
                    print("No expenses recorded yet.")
                else:
                    for number, expense in enumerate(
                        manager.expenses, start=1
                    ):
                        print(f"{number}. {expense}")

            elif choice == "3":
                total = manager.total_expenses()
                print(f"Total expenses: Rs. {total:.2f}")
                print(budget.budget_status(total))

            elif choice == "4":
                keyword = input("Enter category or keyword: ")
                results = manager.search_expenses(keyword)
                for expense in results:
                    print(expense)
                if not results:
                    print("No matching expenses found.")

            elif choice == "5":
                filename = ExpenseReport.export_to_csv(
                    manager.expenses
                )
                print(f"Report exported to {filename}")

            elif choice == "6":
                print("Thank you for using Personal Finance Tracker!")
                break

            else:
                print("Invalid option. Please try again.")

    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
