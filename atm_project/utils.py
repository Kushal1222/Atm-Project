# Utility functions for common operations like validation, confirmation, and formatting

import time

def validate_amount(amount):
    try:
        amt = int(amount)
        if amt > 100:
            return True
        return False
    except ValueError:
        return False

def check_pin(entered, actual):
    return entered == actual

# Finds and returns account dict if account number matches, else returns None
def find_account(account_number, accounts):
    for acc in accounts:
        if acc["account_number"] == account_number:
            return acc
    return None

def typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()

def generate_txn_id(counter):
    return f"PYB-{counter:04d}"

def get_valid_amount(prompt_text="Enter amount: "):
    while True:
        val = input(prompt_text)
        if validate_amount(val):
            return int(val)
        print("❌ Invalid input! Please try again.")

def get_confirmation(message):
    while True:
        ans = input(message).lower()
        if ans == 'y':
            return True
        if ans == 'n':
            return False
        print("❌ Invalid input! Please try again.")
