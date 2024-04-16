# find a transaction to edit ==> selected by user input
# once transaction is found,
# which element (i.e. date, time, cost, etc.) do you want to edit? ==> selected by user input
# possibly isolate the transaction so that there's no side effects ==> overwriting the file
# only changes what the user changed
# then change the item the user wants to edit ==> overwrite the file
from get_input import convert_input_to_datetime
from file_manipulation import get_txt_lines
from datetime import datetime

# we can't use get_txt_lines because
# we need to use the whole txt file, not just a list of the
# items
# we can't rewrite individual text file lines, we can only rewrite the whole file


def edit_transaction():
    user_input_as_date = convert_input_to_datetime()
    # invoke the convert function to declare a variable
    # storing the user inputted date as a datetime object

    # open the trans.txt file with the "read" functionality
    with open("trans.txt", "r") as file:
        # read the lines from the text file and store it in a list
        transactions_list = file.readlines()
    # do the following for each line in the list (use index, each enumerate())
    for index, transaction in enumerate(transactions_list):
        # split the current line and store that new list in a variable
        transaction_split = transaction.split()
        # store the 3rd index of the newly split list in a variable
        date_from_txt_file = transaction_split[3]
        # convert that variable from line 29 into a datetime object
        date_from_txt_as_datetime = datetime.strptime(
            date_from_txt_file, "%Y-%m-%d")
        # compare the datetime object to the user_input_as_date
        if date_from_txt_as_datetime == user_input_as_date:
            # if they are the same, then prompt the user to
            # ask if current iteration is the transaction they want to edit
            print(f"Is {transaction} the transaction you want to edit?")
            answer = input("y/n: ")
            # if user answers yes
            if answer.lower() == "y":
                # print the current line (aka the transaction) and ask the user which index they want to edit
                for index, item in enumerate(transaction_split):
                    print(f"{index}) {item}")
                print("type the number of the item you want to edit")
                ind = int(input())
                # get the new information
                new_information = input(
                    "What would you like to change this item to? ")
                # if the user types in a certain number, go to that index and change it to what the user typed in

                # current_line_split[index] = new_information
                transaction_split[ind] = new_information
                # convert the split list into a string, store it in a variable " ".join(list)
                "".join(transaction_split)
                # at the current iteration's index, replace the information with the variable from line 48

    # open the text file with "write" functionality

    # use the updated list from line 23 and overwrite the txtfile


edit_transaction()

# when running program if two dates are the same it will automaticaly edit both
