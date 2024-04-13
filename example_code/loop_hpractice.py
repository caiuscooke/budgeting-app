# user_input = input("pick the word: ")  # have a input to add to a list
# letter_list = []  # empty list to add info to
# for each in user_input: #for each letter in user_input
#     letter_list.append(each)  # adding the info from the input to the list
# print(letter_list)

# add user innput to the number before
# make user input for whole number
user_input_num = int(input("pick a number.: "))
# empty list to store the number up to given number
user_input_num_list = []
# use a for loop to add numbers to  a list
for num in range(1, user_input_num + 1):  # use range to go from 1 to user input
    # use append to add  the numbers to the list
    user_input_num_list.append(num)
# create a empty num to add to the num from num list
empty_num = 0
final_num_list = []
# for every num in user input list
for num in user_input_num_list:
    # add that number to empty number
    empty_num += num
    # if the num is less than uin -1
    if num < user_input_num - 1:
        # add the num to the uinl num + 1
        num += user_input_num_list[num + 1]
        final_num_list.append(num)
