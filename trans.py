from datetime import datetime

from get_input import get_user_input


class Transaction:
    def __init__(self, category: str, amount: float, time: str, date: str, product: list):
        self.category = category
        self.amount = amount
        self.time = time
        self.date = date
        self.product = product

    # create a txt:
    def save(self):
        with open("trans.txt", "a") as file:
            file.write(
                f"\n{self.category} {self.amount} {self.time} {self.date} {self.product}")


def view():
    with open("trans.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line)


def display_transactions():
    print("Input two digits for the day, month, and year.")
    print("Ex) 07 22 20 for July 22nd, 2000")

    day = get_user_input("Day")
    month = get_user_input("Month")
    year = get_user_input("Year")

    date_string = f"{month}:{day}:{year}"
    user_input_as_date = datetime.strptime(date_string, "%m:%d:%y")

    with open('trans.txt', 'r') as file:
        transactions = file.readlines()
        for transaction in transactions:
            line_split = transaction.split()
            date = line_split[3]  # string date from the txt file
            txt_file_as_date = datetime.strptime(date, "%m:%d:%Y")

            if user_input_as_date == txt_file_as_date:
                print(transaction)
