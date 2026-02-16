from . import database
from .models import Transaction

def display_menu():
    """Displays the main menu to the user."""
    print("\n--- Budget Tracker Menu ---")
    print("1. Add Revenue")
    print("2. Add Expense")
    print("3. View All Transactions")
    print("4. View Balance")
    print("5. Exit")
    print("--------------------")

def get_transaction_details(type):
    """Gets description and amount input from the user."""
    while True:
        description = input(f"Enter the {type} description: ")
        if description:
            break
        else:
            print("Description cannot be empty")
    
    while True:
        try:
            amount_str = input(f"Enter {type} amount: ")
            amount = float(amount_str)
            if amount >= 0:
                return description, amount
            else:
                print('Amount must be non-negative.')
        except ValueError:
            print("Invalid amount. Please enter a number.")

def add_revenue():
    """Adds a revenue transaction."""
    print('\n --- Add Revenue ---')
    description, amount = get_transaction_details('revenue')
    transaction = Transaction(type = 'revenue', description=description, amount=amount)
    database.add_transaction(transaction)

def add_expense():
    """Adds an expense transaction."""
    print('\n --- Add Expense ---')
    description, amount = get_transaction_details('expense')
    transaction = Transaction(type = 'expense', description=description, amount=amount)
    database.add_transaction(transaction)

def view_transactions():
    """Views all transactions."""
    print("\n --- All Transactions ---")
    transactions = database.get_all_transactions()
    if not transactions:
        print("No transactions yet.")
        return
    
    for tx in transactions:
        print(tx.display())
    
    print('-----------------')

def view_balance():
    """Calculates and displays the current balance."""
    print('\n --- Current Balance ---')
    transactions = database.get_all_transactions()
    total_revenue = sum(tx.amount for tx in transactions if tx.type == 'revenue')
    total_expenses = sum(tx.amount for tx in transactions if tx.type == 'expense')
    balance = total_revenue - total_expenses

    print(f"Total Revenue: +{total_revenue:.2f}")
    print(f"Total Expenses: +{total_expenses:.2f}")
    print('-----------------')
    print(f"Current balance: {balance:.2f}")
    print('-----------------')


def run_app():
    """Main application loop."""
    while True:
        display_menu()
        choice = input("Enter your operation (1-5): ")

        if choice == '1':
            add_revenue()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            view_transactions()
        elif choice == '4':
            view_balance()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
        
        input("\n Press Enter to continue...")