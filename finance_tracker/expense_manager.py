from datetime import datetime
from .expense import Expense


class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            return self.expenses.pop(index)
        raise IndexError("Invalid expense number.")

    def search_expenses(self, keyword):
        keyword = keyword.lower()
        return [
            expense for expense in self.expenses
            if keyword in expense.description.lower()
            or keyword in expense.category.lower()
        ]

    def filter_by_category(self, category):
        return [
            expense for expense in self.expenses
            if expense.category.lower() == category.lower()
        ]

    def filter_by_month(self, year, month):
        return [
            expense for expense in self.expenses
            if datetime.strptime(
                expense.date, "%Y-%m-%d"
            ).year == year
            and datetime.strptime(
                expense.date, "%Y-%m-%d"
            ).month == month
        ]

    def total_expenses(self, expenses=None):
        items = self.expenses if expenses is None else expenses
        return sum(expense.amount for expense in items)
