# Utility functions for common operations like validation, confirmation, and formatting

def validate_amount(amount):
    # Check if amount is a valid number and greater than 100
    try:
        amt = int(amount)
        if amt > 100:
            return True
        else:
            return False
    except:
        return False

def check_pin(entered, actual):
    return entered == actual

# Finds and returns account dict if account number matches, else returns None
def find_account(account_number, accounts):
    for acc in accounts:
        if acc["account_number"] == account_number:
            return acc
    return None

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
