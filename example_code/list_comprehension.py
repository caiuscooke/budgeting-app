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
# user_input = int(input()) + 1 # not iterable as an int
# print(sum([num for num in range(1, user_input)]))

# list_of_words = ["apple", "banana", "cherry", "kiwi", "mango"]
# no_a_list = [word for word in list_of_words if "a" not in word]
# print(no_a_list)

new_list_v1 = [num for num in range(10)]
# print(new_list_v1) # 0-9
new_list_v2 = [num + 3 for num in range(10)]
# print(new_list_v2) # 3 - 12
new_list_v3 = [num + 3 for num in range(10) if num < 10]
# print(new_list_v3) # 3 - 10 => real answer 3 - 12
new_list_v4 = [num + 3 for num in range(10) if num < 10 and num % 2 == 0]
# print(new_list_v4) # 3, 5, 7, 9, 11
premade_list = ["cheeseburger", "hamburger", "tacos", "beer", "franks"]
new_list_v5 = [word + " food" for word in premade_list]
# print(new_list_v5) # each word is going to be concatenated with "food"
premade_list = ["cheeseburger", "hamburger", "tacos", "beer", "franks"]
new_list_v6 = [word + " food" for word in premade_list if len(word) > 4]
# print(new_list_v6) # same as before except "beer"
premade_list = ["cheeseburger", "hamburger", "tacos", "beer", "franks"]
new_list_v7 = [
    word*2 
    for word in premade_list 
    if len(word)>=5 and word.count("e")==2]
# print(new_list_v7) # everything but beer => real answer is EMPTY

premade_list = ["cheeseburger", "hamburger", "tacos", "beer", "franks"]
new_list_v8 = [
    word*2 
    for word in premade_list 
    if len(word)//2>=2 or word.count("e")>0]
# print(new_list_v8) # 0, 1, 2, 3, 4

original_list = ["monday", "tuesday", "wednesday", "thursday", "friday"]
first_derivation = [day.split("t")
                    for day in original_list 
                    if day.count("t") >= 1]
print(first_derivation)
second_derivation = [len(day) for day in first_derivation]
print(second_derivation) # 6, 7 
