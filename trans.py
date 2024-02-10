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
    transactions = get_txt_lines(user_input_as_date)

    print(f"Is {transactions} the transaction you'd like to delete?")
    answer = input("Y/N: ")
    if answer.lower() == "y":

        print("which numbers would you like to delete?")
        lines_to_delete = input()
        lines_to_delete_list = lines_to_delete.split()

        for each in lines_to_delete_list:
            if "," in each:
                each = each[:-1]

        lines_to_delete_list = reversed(lines_to_delete_list)
        # w+: it truncates a file, then reads, then writes
        # r+: it doesn't truncate a file, then reads, then writes

        # seek
        # python opens files in a virtual space
        # uses a virtual cursor
        # reads line-end characters to go to the next line

        with open("trans.txt", "r") as file:
            lines = file.readlines()
        with open("trans.txt", "w") as file:
            for index in lines_to_delete_list:
                del lines[int(index)]
            file.writelines(lines)

    elif answer.lower() == "n":
        # get another input for the dates
        pass
    else:
        # get the user to type y or n again
        pass
