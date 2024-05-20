from core import TRANSACTION_FILE_NAME
from datetime import datetime, timedelta
# open the transactions txt file
with open(TRANSACTION_FILE_NAME, "r") as file:
    # store the lines in a list, call it "transactions_list"
    transactions_list = file.readlines()

today_dt = datetime.now()
last_month_int = today_dt.month - 1
first_day_current_month = today_dt.replace(day=1)
last_day_last_month = first_day_current_month - timedelta(days=1)
first_day_last_month = first_day_current_month.replace(month=last_month_int)
last_month_transactions = []
total = 0
# for each line in the transactions list ===>>> for transaction in transactions_list
for transaction in transactions_list:
    transaction_date = transaction.split()[3]
    # 	split the line into its own list, call it "transaction_split"
# 	get the date item out of transaction_split, store it in "transaction_date"
# 	convert transaction_date to a datetime object
    transaction_datetime = datetime.strptime(transaction_date, "%Y-%m-%d")
# 	if the datetime object is between the first day of last month and the last day of last month
    if (first_day_last_month <= transaction_datetime
            and transaction_datetime <= last_day_last_month):
        # 		add LINE to an empty list called "last_month_transactions"
        last_month_transactions.append(transaction)

# for each transaction in last_month_transactions
for transaction in last_month_transactions:
    # 	split the transaction into a second "transaction_split"
    amount = float(transaction.split()[1])
    # 	get the amount from transaction_split and store it in "amount" after casting to float
    # 	add the amount variable to an empty number variable called "total"
    total += amount
    # print "You spent {total} from {first day of last month (i.e. 04.01.24)} to {last day of last month (i.e. 04.30.24)}"
print(
    f" you spent {total} from {first_day_last_month} to {last_day_last_month}")
# open txt file for monthly totals
with open(TRANSACTION_FILE_NAME, "a") as file:
    # 	write total and month name to txt file
    file.write(str(total))
