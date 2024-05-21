from core import TRANSACTION_FILE_NAME
from datetime import datetime, timedelta
from string import ascii_letters

def calculate_monthly_total() -> None:
    today_date = datetime.now().date()
    
    first_day_current_month = today_date.replace(day=1)
    last_month_int = today_date.month - 1
    
    first_day_last_month = first_day_current_month.replace(month=last_month_int)
    last_day_last_month = first_day_current_month - timedelta(days=1)

    with open(TRANSACTION_FILE_NAME, "r") as file:
        transactions_list = file.readlines()
        print(transactions_list)

    last_month_transactions = []
    for transaction in transactions_list:

        if "=" in transaction:
            continue

        transaction_date = transaction.split()[3]
        transaction_datetime = datetime.strptime(transaction_date, "%Y-%m-%d").date()
        if (first_day_last_month <= transaction_datetime
                and transaction_datetime <= last_day_last_month):
            last_month_transactions.append(transaction)

    total = 0
    for transaction in last_month_transactions:
        amount = float(transaction.split()[1])
        total += amount

    confirmation_line = f"=========you spent {total} from {first_day_last_month} to {last_day_last_month}========="

    print(confirmation_line)
    if (confirmation_line + "\n" not in transactions_list
         or confirmation_line not in transactions_list): # ===> WRITE ANOTHER LINE
        with open(TRANSACTION_FILE_NAME, "a") as file:
            file.write(f"\n{confirmation_line}")

    input("Press enter to return to the main menu...")


# open the transactions txt file
    # store the lines in a list, call it "transactions_list"
# for each line in the transactions list ===>>> for transaction in transactions_list
    # split the line into its own list, call it "transaction_split"
    # get the date item out of transaction_split, store it in "transaction_date"
    # convert transaction_date to a datetime object
    # if the datetime object is between the first day of last month and the last day of last month
        # add LINE to an empty list called "last_month_transactions"
# for each transaction in last_month_transactions
    # split the transaction into a second "transaction_split"
    # get the amount from transaction_split and store it in "amount" after casting to float
    # add the amount variable to an empty number variable called "total"
    # print "You spent {total} from {first day of last month (i.e. 04.01.24)} to 
    # {last day of last month (i.e. 04.30.24)}"
# open txt file for monthly totals
    # write total and month name to txt file