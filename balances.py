from datetime import datetime

from core import BALANCE_FILE_NAME, read_file_contents


def convert_datetime(date: str, time: str) -> datetime:
    # 2024-04-01 00:00:00
    return datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M:%S")


def calculate_balance(date: str, time: str, amount: str):

    last_balance = read_file_contents(BALANCE_FILE_NAME)[-1]
    balance_list = last_balance.split()

    balance_amount = float(balance_list[-1])
    amount = float(amount)

    balance_datetime = convert_datetime(balance_list[0], balance_list[1])
    date_time_object = convert_datetime(date, time)
    # this represents the parameters "date" and "time" as one datetime object

    if date_time_object > balance_datetime:
        new_balance = balance_amount + amount

        with open(BALANCE_FILE_NAME, "a") as file:
            confirmation_line = (
                f"\n{date_time_object} current balance is {new_balance:.2f}"
            )
            file.write(confirmation_line)
            print(confirmation_line)
