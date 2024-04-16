# we had to import 2 functions from files and 2 moduels
from get_input import convert_input_to_datetime
from file_manipulation import get_txt_lines
from datetime import datetime
from string import ascii_lowercase


def edit_transaction():
    user_input_as_date = convert_input_to_datetime()
    # we did this because we want to compare datetime objects instead of strings
    # because strings are finnicky, there could be one extra space and the rest
    # is entirely the same but the if statement would say it's false

    # we did this to open the text file in order to interact with its info
    with open("trans.txt", "r") as file:
        # next we took the information from the text file and made it into a list to interact with the info
        transactions_list = file.readlines()
    # each row in text file
    # this for loop goes through the text file list and numbers the items by row
    for index, transaction in enumerate(transactions_list):
        # take each item in the list & split at the space
        transaction_split = transaction.split()
        # next  set the date index as a variable
        date_from_txt_file = transaction_split[3]
        date_from_txt_as_datetime = datetime.strptime(
            date_from_txt_file, "%Y-%m-%d")  # then convert the date into a date time object to compareto the userinput & make sure its the date of the info that needs to be edited

        # comepare both date time  objects to see if they match
        if date_from_txt_as_datetime == user_input_as_date:
            # ask the user if this is the transaction they wanna edit
            print(f"Is {transaction} the transaction you want to edit?")
            answer = input("y/n: ")  # provide a input for the uset to confirm

            if answer.lower() == "y":  # checks to see if user typed a lower case y
                # each item in row
                # numbers each items in split using trasaction_split(items in each rows)
                for option, item in enumerate(transaction_split):
                    # display to the user the number and item at that number 0-5
                    print(f"{option}) {item}")
                # prompt the user to type in the number they want to edit
                print("type the number of the item you want to edit")
                ind = int(input())  # user input for the number they wanna edit

                new_information = input(
                    "What would you like to change this item to? ")  # provide for the information to replace the old info at current spot
                # then add the new information in that spot in the list
                transaction_split[ind] = new_information
                # adds the new entry to the transaction_split with a new line character behind it
                new_transaction_entry = " ".join(transaction_split) + "\n"

                # displays the new info to the user
                print(new_transaction_entry)
                new_information_ok = input(
                    "Is that information correct? [y/n] ")  # confirms if this information is correct
                if new_information_ok.lower() == "y":  # if user confirms with lower case y
                    # add new entry to the oringinal transaction_list at chosen index
                    transactions_list[index] = new_transaction_entry

    with open("trans.txt", "w") as file:  # open the text file again to overwrite the new information
        # over writes the old text file with the new information
        file.writelines(transactions_list)


edit_transaction()
