class Budget:
    def __init__(self, monthly_limit):
        self.monthly_limit = float(monthly_limit)

    def remaining_budget(self, total_expenses):
        return self.monthly_limit - total_expenses

    def is_over_budget(self, total_expenses):
        return total_expenses > self.monthly_limit

    def budget_status(self, total_expenses):
        remaining = self.remaining_budget(total_expenses)

        if remaining < 0:
            return (
                f"Budget exceeded by Rs. "
                f"{abs(remaining):.2f}"
            )

        return f"Remaining budget: Rs. {remaining:.2f}"
