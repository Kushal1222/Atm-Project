# Contains account data dictionary, transactions list, and global counters

accounts = [
    {
        "holder_name": "Kushal",
        "account_number": "1001",
        "pin": "1111",
        "balance": 10000
    },
    {
        "holder_name": "Aditya",
        "account_number": "1002",
        "pin": "2222",
        "balance": 15000
    }
]

# Separate transactions list per account
transactions = {
    "1001": [],
    "1002": []
}
txn_counter = 1
daily_withdrawn = 0
DAILY_LIMIT = 10000
