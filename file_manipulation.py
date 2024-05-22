from datetime import datetime 
from core import TRANSACTION_FILE_NAME, read_file_contents
# importing the datetime class from the datetime module


def get_txt_lines(user_input_as_date: datetime): 
# defining a function with 1 paramater (datetime object)
    
    transactions = read_file_contents(TRANSACTION_FILE_NAME)
    transaction_results = [] 
    # initialize a list to add the transactions at a specific date 
    # AKA the date provided by our parameter
    
    for index, transaction in enumerate(transactions): 
    # make a for loop to access the index and each item in the lines
        
        line_split = transaction.split() 
        # split each transaction to index the date for each transaction

        date = line_split[3]  
        # declare a variable for the date of the transaction
        
        transaction_date_as_datetime = datetime.strptime(date, "%Y-%m-%d") 
        # convert date from txt file line to datetime object
        # so that we can compare dates instead of strings to ensure accuracy

        if user_input_as_date == transaction_date_as_datetime: 
        # compare the date the user input to the date for each transaction 
            
            transaction_results.append(f"{transaction} {index}") 
            # if the two dates match, add it to the transaction results list with the index 

        return transaction_results

