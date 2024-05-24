from balances import calculate_balance
from core import TRANSACTION_FILE_NAME, read_file_contents
from file_manipulation import get_txt_lines
from get_input import *


class Transaction:
    def __init__(self, category: str, amount: str, time: str, date: str, venue: str):
        self.category = category
        self.amount = amount
        self.time = time
        self.date = date
        self.venue = venue

    # create a txt:
    def save(self):
        with open(TRANSACTION_FILE_NAME, "a") as file:
            file.write(
                f"\n{self.date} {self.time} {self.category} {self.amount} {self.venue}")


def add_transaction():

    print("Type in the information based on the prompt")

    category = get_category()
    amount = get_amount()
    time = get_time()
    date = get_date()
    venue = input("Enter the location you made the purchase: ")

    transaction_information = f"{category} {amount} {time} {date} {venue}"
    is_correct = input(f"Is {transaction_information} correct? [y/n]: ")

    if is_correct.lower() == "y":
        new_transaction = Transaction(
            category, amount, time, date, venue
        )
        ###
        new_transaction.save()
        print("The transaction has been saved.")

        calculate_balance(date, time, f"-{amount}")

        add_more = input("Would you like to add another transaction? [y/n]: ")
        if add_more.lower() == "y":
            add_transaction()

    elif is_correct.lower() == "n":
        add_transaction()


def view():
    lines = read_file_contents(TRANSACTION_FILE_NAME)
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

        lines = read_file_contents(TRANSACTION_FILE_NAME)
        with open(TRANSACTION_FILE_NAME, "w") as file:
            for index in lines_to_delete_list:
                del lines[int(index)]
            file.writelines(lines)

    elif answer.lower() == "n":
        # get another input for the dates
        pass
    else:
        # get the user to type y or n again
        pass
