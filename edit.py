# def get_edit_info():
#     from datetime import datetime
#     from get_input import convert_input_to_datetime
#     from file_manipulation import get_txt_lines
#     print("do you want to edit one  or multiple transactions")
#     print("What do you want to edit in transactions?: date, category, amount, time")
#     user_input_as_date = input()
#     user_input_as_date = convert_input_to_datetime()
#     transactions = get_txt_lines(user_input_as_date)
#     edit_item_list = transactions
#     for  in edit_item_list:

# find a transaction to edit ==> selected by user input
# once transaction is found, 
# which element (i.e. date, time, cost, etc.) do you want to edit? ==> selected by user input
# possibly isolate the transaction so that there's no side effects ==> overwriting the file 
# only changes what the user changed
# then change the item the user wants to edit ==> overwrite the file
from get_input import convert_input_to_datetime
from file_manipulation import get_txt_lines

def edit_transaction():
    user_input_as_date = convert_input_to_datetime()
    transactions = get_txt_lines(user_input_as_date)    
    # we can't use get_txt_lines because
    # we need to use the whole txt file, not just a list of the 
    # items 
    
    # for loop
    # split and see if date matches user_input_as_date
    # nested loop for each item in that split
    # make the edits in the nested for loop