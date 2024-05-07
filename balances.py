from datetime import datetime

def convert_datetime(date:str, time:str) -> datetime:

def calculate_balance(date: str, time: str, amount: str):
    # if the transaction date is after the last line's date or last lines time at the same date in balances.txt
    # subtract the amount of the transaction from that balance
    # write a new balance line in balances.txt (using the subtraction we did before)
    with open("balances.txt", "r") as file:
        balances = file.readlines()[-1]
    balances_list = balances.split()
    balance_date = balances_list[0]
    balance_amount = balances_list[-1]

    if balance_date == date:
