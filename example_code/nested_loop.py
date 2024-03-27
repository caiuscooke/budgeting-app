# ["trans1", "trans2", "trans3"]
# # ask the user which of the transactions they want to edit?
# ["trans1", "trans3"]
# # get rid of the trans items the user doesn't want
# # make a seperate list for each transaction item
# trans1list = ["amount", "category", "date", "time"]
# # now we can index through transXlist to make the edits
# # lets say the user wants to make an edit on date
# # well loop through the transXlist until we find date
# # then, we'll replace whatever was there with the new user edit
# trans1list[2] = "somenewdate"


# # how to do this with a nested loop? VVVV
# transactions_results = [
#     "food 27 12:30am 8:23:2023", "food 27 12:30am 8:23:2023"]
# print(f"Which of these would you like to edit? {transactions_results}")
# selection = input("Enter a number: ")
# # handle when the user wants to only edit a few of the transactions from results
# for ind, each in enumerate(transactions_results):
#     transXlist = each.split()
#     category_to_edit = input("Enter 1-4 to choose an item to edit: ")

#     for index, items in enumerate(transXlist):

#         if index == int(category_to_edit) - 1:
#             change = input("Type the change you would like to make: ")
#             transXlist[index] = change
#             transactions_results[ind] = " ".join(transXlist)


# print(transactions_results)


# nested loops accessing list elements

list_of_list = [["list1 item1", "list1 item2", "list1 item3"],
                ["list2 item1", "list2 item2", "list2 item3"],
                ["list3 item1", "list3 item2", "list3 item3"]]

# list_of_list[0][0] = "hello"
# print(list_of_list)
for out_index, list in enumerate(list_of_list):
    for in_index, string in enumerate(list):
        list_of_list[out_index][in_index] = string.split()

    print(list_of_list[out_index])


print(list_of_list)



for i in range(0, -10, -4):
    print(i)
    for j in range(0, -4, 1):
        print(i, end=" ")
    print("", end="\n")

# 0
# 
# -4 
    
#     0
#    000
#   00000
#  0000000
# 000000000

for x in range(0, 6):
    for y in range(0, 6 - x):
        print(" ", end="")
    for z in range(0, 2*x+1):
        print("0", end="")
    print("")
