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

def add_transaction():
    # add function pseudo
    # print instruction to user
    print("Type in the information based on the prompt")
    # create an empty list
    transaction_information = []
    # make a list for the prompts
    prompts = ["Category: ", "Amount: ", "Time: ", "Date: ", "Products Bought: "]
    # make a for loop where each iteration
    for prompt in prompts: 
    # we get user input
        information = input()
    # append user's input to the list
        transaction_information.append(information)
    # prompt user to confirm information is correct
    is_correct = input(f"Is {" ".join(transaction_information)} correct? [y/n]: ")
    # if yes
    if is_correct.lower() == "y":
    #   create an instance with the information gathered
        new_transaction = Transaction(
            transaction_information[0], transaction_information[1],
            transaction_information[2], transaction_information[3],
            transaction_information[4]
        )
    #   on that instance, call the save function
        new_transaction.save()
    #   inform user of successful save
        print("The transaction has been saved.")
    #   ask user if they'd like to add another
        add_more = input("Would you like to add another transaction? [y/n]: ")
        

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
