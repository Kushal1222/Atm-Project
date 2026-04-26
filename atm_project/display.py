# Functions for displaying menus, banners, receipts, and formatting boxes

def show_banner():
    print("W e l c o m e   t o   P y B a n k   A T M . . .")
    print("========================================")
    print("     🏦  PyBank ATM  🏦")
    print("     India's Smart Virtual ATM")
    print("========================================")

def show_menu():
    print("========================================")
    print("       🏧  PyBank ATM - MENU")
    print("========================================")
    print("  1. Check Balance")
    print("  2. Deposit Money")
    print("  3. Withdraw Money")
    print("  4. View Full Statement")
    print("  5. Mini Statement")
    print("  6. Exit")
    print("========================================")

def show_receipt(txn):
    print("========================================")
    print("         TRANSACTION RECEIPT")
    print("========================================")
    print(f"  TXN ID   : {txn['txn_id']}")
    print(f"  Type     : {txn['type']}")
    print(f"  Amount   : Rs. {txn['amount']:,}")
    print(f"  Date     : {txn['date']}")
    print(f"  Balance  : Rs. {txn['balance']:,}")
    print("========================================")
    print("    Thank you for banking with us!")
    print("========================================")

def print_box(message):
    print("========================================")
    print(message)
    print("========================================")

def show_account_details(account):
    print("========================================")
    print("          ACCOUNT DETAILS")
    print("========================================")
    print(f"  Name    : {account['holder_name']}")
    print(f"  Acct No : {account['account_number']}")
    print(f"  Balance : Rs. {account['balance']:,}")
    print("========================================")
