# Functions handling core business logic for ATM transactions (deposit, withdraw, statement etc)

from datetime import datetime
from utils import generate_txn_id, get_valid_amount, get_confirmation, typing_effect
from display import show_receipt, print_box

def deposit(account, transactions, counter):
    amount = get_valid_amount("Enter amount to deposit: ")
    if not get_confirmation(f"Are you sure you want to deposit Rs. {amount}? (y/n): "):
        print("Transaction cancelled.")
        return counter

    account['balance'] += amount
    txn_id = generate_txn_id(counter)
    counter += 1
    
    dt_str = datetime.now().strftime("%d-%m-%Y  %I:%M %p")
    txn = {
        "txn_id": txn_id,
        "type": "Deposit",
        "amount": amount,
        "date": dt_str,
        "balance": account['balance']
    }
    transactions.append(txn)
    show_receipt(txn)
    return counter

def withdraw(account, transactions, counter, daily_withdrawn):
    DAILY_LIMIT = 10000
    LOW_BALANCE_LIMIT = 1000
    
    amount = get_valid_amount("Enter amount to withdraw: ")
    if not get_confirmation(f"Are you sure you want to withdraw Rs. {amount}? (y/n): "):
        print("Transaction cancelled.")
        return counter, daily_withdrawn

    if amount > account['balance']:
        shortfall = amount - account['balance']
        print("❌ Insufficient Funds!")
        print(f"   You need Rs. {shortfall:,} more to complete this.")
        return counter, daily_withdrawn
    
    if daily_withdrawn + amount > DAILY_LIMIT:
        print(f"⚠️  Daily withdrawal limit of Rs. {DAILY_LIMIT:,} reached!")
        return counter, daily_withdrawn

    account['balance'] -= amount
    daily_withdrawn += amount
    
    print("✅ Withdrawal Successful!")
    print(f"💰 Remaining daily limit : Rs. {DAILY_LIMIT - daily_withdrawn:,}")
    
    if account['balance'] < LOW_BALANCE_LIMIT:
        print(f"⚠️  Low Balance Warning! Your balance is below Rs. {LOW_BALANCE_LIMIT:,}.")
        
    txn_id = generate_txn_id(counter)
    counter += 1
    
    dt_str = datetime.now().strftime("%d-%m-%Y  %I:%M %p")
    txn = {
        "txn_id": txn_id,
        "type": "Withdraw",
        "amount": amount,
        "date": dt_str,
        "balance": account['balance']
    }
    transactions.append(txn)
    show_receipt(txn)
    return counter, daily_withdrawn

def view_statement(transactions, account):
    if not transactions:
        print("No transactions found.")
        return

    print("---------------------------------------------------------------")
    print("Sr  | TXN ID   | Type     | Amount    | Date & Time    | Balance")
    print("---------------------------------------------------------------")
    
    for i, txn in enumerate(transactions, 1):
        amt_str = f"Rs. {txn['amount']}"
        bal_str = f"Rs. {txn['balance']:,}"
        try:
            dt_short = datetime.strptime(txn['date'], "%d-%m-%Y  %I:%M %p").strftime("%d-%m-%y %H:%M")
        except ValueError:
            dt_short = txn['date']
        print(f" {i:<2} | {txn['txn_id']:<8} | {txn['type']:<8} | {amt_str:<9} | {dt_short} | {bal_str}")
        
    print("---------------------------------------------------------------")
    
    total_dep = sum(t['amount'] for t in transactions if t['type'] == 'Deposit')
    total_with = sum(t['amount'] for t in transactions if t['type'] == 'Withdraw')
    print(f"  Total Deposited  : Rs. {total_dep:,}")
    print(f"  Total Withdrawn  : Rs. {total_with:,}")
    print(f"  Current Balance  : Rs. {account['balance']:,}")
    print("---------------------------------------------------------------")

def mini_statement(transactions):
    if not transactions:
        print("No transactions found.")
        return
        
    mini_txns = transactions[-3:]
    print("---------------------------------------------------------------")
    print("Sr  | TXN ID   | Type     | Amount    | Date & Time    | Balance")
    print("---------------------------------------------------------------")
    
    for i, txn in enumerate(mini_txns, 1):
        amt_str = f"Rs. {txn['amount']}"
        bal_str = f"Rs. {txn['balance']:,}"
        try:
            dt_short = datetime.strptime(txn['date'], "%d-%m-%Y  %I:%M %p").strftime("%d-%m-%y %H:%M")
        except ValueError:
            dt_short = txn['date']
        print(f" {i:<2} | {txn['txn_id']:<8} | {txn['type']:<8} | {amt_str:<9} | {dt_short} | {bal_str}")
        
    print("---------------------------------------------------------------")

def change_pin(account):
    while True:
        old_pin = input("Enter old PIN: ")
        if old_pin != account['pin']:
            print("❌ Incorrect PIN! PIN change failed.")
            return
            
        new_pin = input("Enter new PIN (4 digits): ")
        confirm_pin = input("Confirm new PIN: ")
        
        if new_pin != confirm_pin:
            print("❌ PINs do not match! Try again.")
        else:
            account['pin'] = new_pin
            print("✅ PIN changed successfully!")
            break
