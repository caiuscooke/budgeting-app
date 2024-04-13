# add user innput to the number before
# create a int user input and empty list to store the range of numbers
# use a for loop & range to add the numbers to the empty list
num_user_input = int(input("enter your number.: "))
num_user_input_list = []
for num in range(1, num_user_input+1):
    num_user_input_list.append(num)
print(num_user_input_list)
# create a empty num to add the numbers from the list too
# create a empty list to store the final values in
#use a second for loop to add the numbers from the list to empty num
#if the num is less than the user input -1
# num += to to the [num + 1]
#append the new empty list with the num values
empty_num = 0
final_num_list = []
for num in num_user_input_list:
    empty_num += num
    if num < num_user_input - 1:
        num += num_user_input_list[num + 1]
        final_num_list.append(num)
