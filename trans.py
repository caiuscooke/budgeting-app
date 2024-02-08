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
    transactions = get_txt_lines(user_input_as_date)  # [1, 3, 5, 16, 18, 20]

    print(f"Is {transactions} the transaction you'd like to delete?")
    answer = input("Y/N: ")  # y n
    if answer.lower() == "y":
        # would you like to delete 1 or multiple items?
        print("would you like to delete 1 or multiple items?")
        # accept user input - "1" or "multiple"
        choice = input()
        # if multiple
        if "multiple" == choice:
            # which numbers would you like to delete?
            print("which numbers would you like to delete?")
            lines_to_delete = input()
            lines_to_delete_list = lines_to_delete.split()
            # ["1,", "3,", "16,", "20"]
            for each in lines_to_delete_list:
                if "," in each:
                    each = each[:-1]

            # ["1", "3", "16", "20"]
            # delete the remaining items in the transactions list from the txt file
            with open("trans.txt", "w") as file:
                lines = file.readlines()
                for index in lines_to_delete_list:
                    # go to the specific line in the file
                    # and delete it
                    del lines[index]
                file.write(lines)
    elif answer.lower() == "n":
        # get another input for the dates
        pass
    else:
        # get the user to type y or n again
        pass
