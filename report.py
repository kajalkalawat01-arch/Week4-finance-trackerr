import csv


class ExpenseReport:
    @staticmethod
    def export_to_csv(expenses, filename="expenses_report.csv"):
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "date",
                    "amount",
                    "category",
                    "description",
                ],
            )
            writer.writeheader()

            for expense in expenses:
                writer.writerow(expense.to_dict())

        return filename

    @staticmethod
    def category_summary(expenses):
        summary = {}

        for expense in expenses:
            summary[expense.category] = (
                summary.get(expense.category, 0) + expense.amount
            )

        return summary
