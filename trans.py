from datetime import datetime

from get_input import convert_input_to_datetime
from file_manipulation import get_txt_lines


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
    user_input_as_date = convert_input_to_datetime()
    transaction = get_txt_lines(user_input_as_date)

    print(transaction)


def delete_transaction():
    user_input_as_date = convert_input_to_datetime()
    transaction = get_txt_lines(user_input_as_date)

    print(f"Is {transaction} the transaction you'd like to delete?")
    answer = input("Y/N: ")  # y n
    if answer.lower() == "y":
        # delete
        pass
    elif answer.lower() == "n":
        # get another input for the dates
        pass
    else:
        # get the user to type y or n again
        pass
