# user types in a word, we want each letter in a list
# user_input = input()
# empty_list = []
# for each in user_input:
#     if each != "l":
#         each += "%"
#         empty_list.append(each)
# print(empty_list)

# doing this in one line VVVV
# user_input = input()
# char_list = [char + "%" for char in user_input if char != "l"]
# print(char_list)

# newlist = [expression for item in iterable if condition == True]

# Calculate the sum of all numbers from 1 to a given number
# Write a program to accept a number from a user 
# and calculate the sum of all numbers from 1 to a given number
# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
# using sum() is fine
user_input = int(input()) + 1 # not iterable as an int
print(sum([num for num in range(1, user_input)]))

list_of_words = ["apple", "banana", "cherry", "kiwi", "mango"]
no_a_list = [word for word in list_of_words if "a" not in word]
print(no_a_list)