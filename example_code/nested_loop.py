["trans1", "trans2", "trans3"]
# ask the user which of the transactions they want to edit?
["trans1", "trans3"]
# get rid of the trans items the user doesn't want
# make a seperate list for each transaction item
trans1list = ["amount", "category", "date", "time"]
# now we can index through transXlist to make the edits
# lets say the user wants to make an edit on date
# well loop through the transXlist until we find date
# then, we'll replace whatever was there with the new user edit
trans1list[2] = "somenewdate"


# how to do this with a nested loop? VVVV
transactions_results = [
    "food 27 12:30am 8:23:2023", "food 27 12:30am 8:23:2023"]
print(f"Which of these would you like to edit? {transactions_results}")
selection = input("Enter a number: ")
# handle when the user wants to only edit a few of the transactions from results
for ind, each in enumerate(transactions_results):
    transXlist = each.split()
    category_to_edit = input("Enter 1-4 to choose an item to edit: ")

    for index, items in enumerate(transXlist):

        if index == int(category_to_edit) - 1:
            change = input("Type the change you would like to make: ")
            transXlist[index] = change
            transactions_results[ind] = " ".join(transXlist)


print(transactions_results)
