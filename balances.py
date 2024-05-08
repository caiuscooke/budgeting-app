from datetime import datetime


def convert_datetime(date: str, time: str) -> datetime:
    # 2024-04-01 00:00:00
    return datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S")


def calculate_balance(date: str, time: str, amount: str):

    with open("balances.txt", "r") as file:
        balances = file.readlines()[-1]
    balances_list = balances.split()

    balance_amount = float(balances_list[-1])
    amount = float(amount)

    balance_datetime = convert_datetime(balances_list[0], balances_list[1])
    date_time_object = convert_datetime(date, time)

    if date_time_object > balance_datetime:
        new_balance = balance_amount + amount

        with open("balances.txt", "a") as file:
            confirmation_line = f"\n{date_time_object} current balance is {new_balance:.2f}"
            file.write(confirmation_line)
            print(confirmation_line)

