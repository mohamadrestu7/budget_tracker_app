import sqlite3
from .models import Transaction

DB_FILE = 'budget.db'

def get_db_connection():
    """Establishes the connection to the SQLite database."""
    conn = sqlite3.connect(DB_FILE)
    # Return rows as objects that behave like dictionaries
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes the database and create the transactions table if it doesn't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   type TEXT NOT NULL CHECK(type IN ('revenue', 'expense')),
                   description TEXT NOT NULL,
                   amount REAL NOT NULL,
                   date TEXT NOT NULL
                   )
    """)
    conn.commit()
    conn.close()
    print("Database initialized.")

def add_transaction(transaction: Transaction):
    """Adds a new transaction to the database."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(""" 
            INSERT INTO transactions (type, description, amount, date)
                   VALUES (?, ?, ?, ?)        
    """, (transaction.type, transaction.description, transaction.amount, transaction.date))
    conn.commit()
    conn.close()
    print(f"{transaction.type.capitalize()} added successfully.")

def get_all_transactions():
    """Retrieves all transactions from the database, ordered by date."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()

    transactions = [
        Transaction(id=row['id'], type=row['type'], description=row['description'],
                    amount=row['amount'], date=row['date'])
                    for row in rows
    ]

    return transactions