from datetime import datetime

from core import TRANSACTION_FILE_NAME, read_file_contents
from get_input import convert_input_to_datetime


def get_index_to_edit(transaction_split: list) -> int:
    """
    this function takes a list and prints out each item with a number (aka it's index) next to it
    then it accepts an input so the user can choose an item from that list
    """
    # block comments

    # adds a number for each item that was split at the space in the transaction
    for option, item in enumerate(transaction_split):
        # display to the user the number and item at that number 0-5
        print(f"{option}) {item}")
    # prompt the user to type in the number they want to edit
    print("type the number of the item you want to edit")
    return int(input())
    # since we used enumerate to display each item, the number the user types in
    # is going to be equal to the index of that item, allowing us to use it later in the code


def get_date_from_transaction(transaction: str) -> datetime:
    # take each item in the list & split at the space
    transaction_as_list = transaction.split()

    # next set the date index as a variable
    # then convert the date into a datetime object to compare to the userinput
    # check comment after line 9 for why
    date_from_txt_file = transaction_as_list[0]

    return datetime.strptime(date_from_txt_file, "%Y-%m-%d")


def edit_transaction():
    user_input_as_date = convert_input_to_datetime()
    # we did this because we want to compare datetime objects instead of strings
    # because strings are finnicky, there could be one extra space and the rest
    # is entirely the same but the if statement would say it's false

    transactions_list = read_file_contents(TRANSACTION_FILE_NAME)

    # this for loop goes through the text file list and numbers the items by row
    for index, transaction in enumerate(transactions_list):

        datetime_from_transaction = get_date_from_transaction(transaction)

        # compare both datetime objects to see if they match
        if datetime_from_transaction == user_input_as_date:
            # confirm before moving on that this is the transaction that needs to be edited
            print(f"Is {transaction} the transaction you want to edit?")
            answer = input("y/n: ")  # provide an input for the user to confirm

            if answer.lower() == "n":  # convert user answer to lowercase to prevent false negative
                continue

            transaction_split = transaction.split()
            user_selection = get_index_to_edit(transaction_split)

            new_information = input(
                "What would you like to change this item to? ")
            # provide input for the information to replace the old info at current spot

            # then add the new information using the index of it (AKA the number the user typed in, line 47)
            # adds the information to the split list, not the original so we can confirm to the user before
            # making permanent changes
            transaction_split[user_selection] = new_information

            # create a variable storing the string representation of the new information
            # this allows us to put it back into the original list (added a new line character to
            # eliminate conflicts with adding it to the txt file)
            new_transaction_entry = " ".join(transaction_split) + "\n"

            # displays the new info to the user
            print(new_transaction_entry)
            new_information_ok = input(
                "Is that information correct? [y/n] ")
            # gets user confirmation that this information is correct

            if new_information_ok.lower() == "y":
                # use lower to convert user input to a lowercase letter
                # just in case they typed capital Y, this won't be a false negative

                # add new entry to the original transaction_list at current iteration's index
                transactions_list[index] = new_transaction_entry

    with open("trans.txt", "w") as file:  # open the text file again to overwrite the new information
        # over writes the old text file with the new information
        file.writelines(transactions_list)
