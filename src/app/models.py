import datetime

class Transaction:
    """Represents a single financial transaction."""
    def __init__(self, type, description, amount, date=None, id=None):
        # Validate the type
        if type not in ['revenue', 'expense']:
            raise ValueError("Transaction type must be 'revenue' or 'expense'")
        
        # Validate the amount
        if not isinstance(amount, (int, float)) or amount < 0:
            raise ValueError("Amount must be non-negative.")
        
        self.id = id
        self.type = type
        self.description = description
        self.amount = float(amount)
        self.date = datetime.datetime.today().isoformat()

    def __repr__(self):
        """Provides a developer-friendly string representation."""
        return (f"""Transaction(id={self.id}), type = {self.type},\n
                 description='{self.description}, amount={self.amount:.2f},"
                 date='{self.date}') """)
    
    def display(self):
        """Provides a user_friendly string representation."""
        symbol = "+" if self.type == 'revenue' else "-"
        return f"[{self.date}] {symbol}{self.amount:.2f}: {self.description}"