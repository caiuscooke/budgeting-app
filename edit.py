# find a transaction to edit ==> selected by user input
# once transaction is found, 
# which element (i.e. date, time, cost, etc.) do you want to edit? ==> selected by user input
# possibly isolate the transaction so that there's no side effects ==> overwriting the file 
# only changes what the user changed
# then change the item the user wants to edit ==> overwrite the file
from get_input import convert_input_to_datetime
from file_manipulation import get_txt_lines
from datetime import datetime

def edit_transaction():
    user_input_as_date = convert_input_to_datetime()
    # we can't use get_txt_lines because
    # we need to use the whole txt file, not just a list of the 
    # items 
    
    # for loop
    # split and see if date matches user_input_as_date
    # nested loop for each item in that split
    # make the edits in the nested for loop