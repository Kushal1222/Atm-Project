# Entry point for the PyBank ATM Simulation project. Handles authentication and menu loop.

from datetime import datetime
import account as data
import display
import transactions
from utils import check_pin, find_account

def main():
    display.show_banner()
    
    attempts = 0
    logged_in = False
    
    while True:
        acc_no = input("Enter Account Number: ")
        current_account = find_account(acc_no, data.accounts)
        if current_account is None:
            print("❌ Account not found! Please check your account number.")
        else:
            break

    while attempts < 3:
        pin = input("Enter PIN: ")
        
        if check_pin(pin, current_account['pin']):
            logged_in = True
            print("----------------------------------------")
            print("✅ Login Successful!")
            print(f"Welcome back, {current_account['holder_name']}!")
            print("----------------------------------------")
            break
        else:
            attempts += 1
            if attempts < 3:
                print("❌ Invalid input! Please try again.")
            
    if not logged_in:
        print("========================================")
        print("🔒 Card Blocked! Please contact bank.")
        print("========================================")
        return
        
    while True:
        display.show_menu()
        
        choice_str = input("Enter your choice: ")
        try:
            choice = int(choice_str)
            if choice < 1 or choice > 6:
                print("❌ Invalid choice! Enter a number between 1 and 6.")
                continue
        except ValueError:
            print("❌ Invalid input! Please try again.")
            continue
            
        if choice == 1:
            display.show_account_details(current_account)
        elif choice == 2:
            acc_no = current_account['account_number']
            acc_txns = data.transactions[acc_no]
            data.txn_counter = transactions.deposit(current_account, acc_txns, data.txn_counter)
        elif choice == 3:
            acc_no = current_account['account_number']
            acc_txns = data.transactions[acc_no]
            data.txn_counter, data.daily_withdrawn = transactions.withdraw(current_account, acc_txns, data.txn_counter, data.daily_withdrawn)
        elif choice == 4:
            transactions.view_statement(data.transactions[current_account['account_number']], current_account)
        elif choice == 5:
            transactions.mini_statement(data.transactions[current_account['account_number']])
        elif choice == 6:
            dt_str = datetime.now().strftime("%I:%M %p")
            print("========================================")
            print("👋 Thank you for using PyBank ATM!")
            print(f"   Session ended at {dt_str}")
            print(f"   Have a great day, {current_account['holder_name']}!")
            print("========================================")
            break

if __name__ == "__main__":
    main()
