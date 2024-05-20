from core import TRANSACTION_FILE_NAME
from datetime import datetime, timedelta
# open the transactions txt file
with open(TRANSACTION_FILE_NAME, "r") as file:
    # store the lines in a list, call it "transactions_list"
    transactions_list = file.readlines()

input_dt = datetime.now()
last_month = input_dt.month - 1
first_date = input_dt.replace(day=1)
last = first_date - timedelta(days=1)
lastmonth = first_date.replace(month=last_month)
print(first_date, last, lastmonth)
# for each line in the transactions list ===>>> for transaction in transactions_list
for transaction in transactions_list:
    # 	split the line into its own list, call it "transaction_split"
    transaction_date = transaction.split()[3]
# 	get the date item out of transaction_split, store it in "transaction_date"
# 	convert transaction_date to a datetime object
    transaction_datetime = datetime.strptime(transaction_date, "%Y-%m-%d")
# 	if the datetime object is between the first day of last month and the last day of last month
if lastmonth <= transaction_datetime and transaction_datetime <= last:
    # 		add LINE to an empty list called "last_month_transactions"

    # for each transaction in last_month_transactions
    # 	split the transaction into a second "transaction_split"
    # 	get the amount from transaction_split and store it in "amount" after casting to float
    # 	add the amount variable to an empty number variable called "total"

    # print "You spent {total} from {first day of last month (i.e. 04.01.24)} to {last day of last month (i.e. 04.30.24)}"
    # open txt file for monthly totals
    # 	write total and month name to txt file
