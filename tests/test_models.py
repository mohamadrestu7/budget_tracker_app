import pytest
import datetime
from src.app.models import Transaction

def test_create_valid_revenue_transaction():
    """Tests creating a valid revenue transaction with default date."""
    tx = Transaction(type='revenue', description='Salary', amount = 5000.0)
    assert tx.id is None
    assert tx.type == 'revenue'
    assert tx.description == 'Salary'
    assert tx.amount == 5000.0
    assert tx.date == datetime.datetime.today().isoformat()

def test_create_valid_expense_transaction():
    """Tests creating a valid expense transaction with default date."""
    tx = Transaction(type='expense', description='Food', amount = 500.0)
    assert tx.id is None
    assert tx.type == 'expense'
    assert tx.description == 'Food'
    assert tx.amount == 500.0
    assert tx.date == datetime.datetime.today().isoformat()

def test_transaction_display_revenue():
    """Tests the user-friendly format for revenue."""
    tx = Transaction(type = 'revenue', description='Consulting', amount = 500)
    assert tx.display() == f"[{datetime.datetime.today().isoformat()}] +500.00: Consulting"
    # return f"[{self.date}] {symbol}{self.amount:.2f}: {self.description}"