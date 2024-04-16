from get_input import convert_input_to_datetime
from file_manipulation import get_txt_lines
from datetime import datetime
from string import ascii_lowercase


def edit_transaction(): 
    user_input_as_date = convert_input_to_datetime()
    # we did this because we want to compare datetime objects instead of strings
    # because strings are finnicky, there could be one extra space and the rest
    # is entirely the same but the if statement would say it's false

    with open("trans.txt", "r") as file:
        transactions_list = file.readlines()

    for index, transaction in enumerate(transactions_list):
        transaction_split = transaction.split()
        date_from_txt_file = transaction_split[3]
        date_from_txt_as_datetime = datetime.strptime(
            date_from_txt_file, "%Y-%m-%d")

        if date_from_txt_as_datetime == user_input_as_date:
            print(f"Is {transaction} the transaction you want to edit?")
            answer = input("y/n: ")

            if answer.lower() == "y":

                for option, item in enumerate(transaction_split):
                    print(f"{option}) {item}")
                print("type the number of the item you want to edit")
                ind = int(input())

                new_information = input(
                    "What would you like to change this item to? ")
                transaction_split[ind] = new_information
                new_transaction_entry = " ".join(transaction_split) + "\n"

                print(new_transaction_entry)
                new_information_ok = input(
                    "Is that information correct? [y/n] ")
                if new_information_ok.lower() == "y":
                    transactions_list[index] = new_transaction_entry

    with open("trans.txt", "w") as file:
        file.writelines(transactions_list)


edit_transaction()
