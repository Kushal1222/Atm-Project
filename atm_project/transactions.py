# Functions handling core business logic for ATM transactions (deposit, withdraw, statement etc)

from datetime import datetime
from utils import generate_txn_id, get_valid_amount, get_confirmation, typing_effect
from display import show_receipt, print_box

def deposit(account, transactions, counter):
    amount = get_valid_amount("Enter amount to deposit: ")
    if not get_confirmation(f"Are you sure you want to deposit Rs. {amount}? (y/n): "):
        print("Transaction cancelled.")
        return counter

    account['balance'] = account['balance'] + amount
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

    account['balance'] = account['balance'] - amount
    daily_withdrawn = daily_withdrawn + amount
    
    print("✅ Withdrawal Successful!")
    remaining = DAILY_LIMIT - daily_withdrawn
    print(f"💰 Remaining daily limit : Rs. {remaining}")
    
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
        print(f"  {i} | {txn['txn_id']} | {txn['type']} | Rs.{txn['amount']} | {txn['date']} | Rs.{txn['balance']}")
        
    print("---------------------------------------------------------------")
    
    total_dep = 0
    total_with = 0
    for t in transactions:
        if t['type'] == 'Deposit':
            total_dep = total_dep + t['amount']
        if t['type'] == 'Withdraw':
            total_with = total_with + t['amount']
    print(f"  Total Deposited  : Rs. {total_dep:,}")
    print(f"  Total Withdrawn  : Rs. {total_with:,}")
    print(f"  Current Balance  : Rs. {account['balance']:,}")
    print("---------------------------------------------------------------")

def mini_statement(transactions):
    if not transactions:
        print("No transactions found.")
        return
        
    total = len(transactions)
    if total >= 3:
        mini_txns = transactions[total - 3 : total]
    else:
        mini_txns = transactions
    print("---------------------------------------------------------------")
    print("Sr  | TXN ID   | Type     | Amount    | Date & Time    | Balance")
    print("---------------------------------------------------------------")
    
    for i, txn in enumerate(mini_txns, 1):
        print(f"  {i} | {txn['txn_id']} | {txn['type']} | Rs.{txn['amount']} | {txn['date']} | Rs.{txn['balance']}")
        
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
