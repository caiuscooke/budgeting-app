# open the transactions txt file
# store the lines in a list, call it "transactions_list"

# for each line in the transactions list ===>>> for transaction in transactions_list
# 	split the line into its own list, call it "transaction_split"
# 	get the date item out of transaction_split, store it in "transaction_date"
# 	convert transaction_date to a datetime object
# 	if the datetime object is between the first day of last month and the last day of last month
# 		add LINE to an empty list called "last_month_transactions"

# for each transaction in last_month_transactions
# 	split the transaction into a second "transaction_split"
# 	get the amount from transaction_split and store it in "amount" after casting to float
# 	add the amount variable to an empty number variable called "total"

# print "You spent {total} from {first day of last month (i.e. 04.01.24)} to {last day of last month (i.e. 04.30.24)}"
# open txt file for monthly totals
# 	write total and month name to txt file