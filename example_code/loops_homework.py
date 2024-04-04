# PROBLEM1
"""
# make a for loop that adds each letter of the a word to a list
user_input = input()
characters_list = []

for each in user_input:
    characters_list.append(each)
print(characters_list)
"""

# PROBLEM2 
"""
# make a for loop that checks if a letter in a word occurs 2 or more times
user_input = input()
repeating_letters = []
for each in user_input:
    repeat_count = user_input.count(each)
    if repeat_count > 1:
        repeating_letters.append(f"{each}{repeat_count}")

# HOW DO WE SHOW THE USER WHICH LETTERS ARE REPEATED?

# METHOD 1
# REMOVES DUPLICATES FROM A LIST BY CASTING TO SET
# BEHIND THE SCENES, A SET DOES THE FOLLOWING
# cheese -> repeating_letters=[e3, e3, e3] -> set(repeating_letters) -> (e3)
repeating_letters_set = set(repeating_letters) 
print(repeating_letters_set)

# METHOD 2
# MAKE AN EMPTY LIST AND ADD THE LETTER FROM "repeating_list" TO IT
# IF THAT LETTER IS ALREADY IN THE LIST, SKIP IT
# PRINT THE "repeating_list" AT THE END
printed_letter = []
for each in repeating_letters:
    if each not in printed_letter:
        printed_letter.append(each)
        print(each)
"""

# PROBLEM3
"""
# make a for loop that adds a random word to each entry in a list
# ["hello", "world"] -> ["hello randomword1", "world randomword2"]

from string import ascii_uppercase
import random

# CHANGED VARIABLE NAME "words_list" -> "random_words_list"
random_words_list = ["cheese", "doodle", "cash", 
                     "code", "learn"]  
test_list = ["hello", "word"]

# CHANGED VARIABLE NAME "test" -> "word"
for index, word in enumerate(test_list):  
    random_word = random.choice(random_words_list)
    test_list[index] += random_word

# TOOK THIS FROM INSIDE THE LOOP SCOPE TO OUTSIDE THE LOOP SCOPE
print(test_list)  
"""


# ANYTIME YOU WANT TO MODIFY THE CURRENT INSTANCE IN THE LOOP
# use "for index, each in enumerate(iterable):"
# (each is the individual item, iterable is the list\string\dictionary\etc.)
# in the loop itself, change the current instance with "iterable[index] = new_item"

# PROBLEM4
"""
# The function takes a single parameter, which is a string.
# Your function should return a list of all the indexes
# in the string that have capital letters.
# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

def get_capital_indexes(word_to_check: str):
    capital_indexes = []
    for index, letter in enumerate(word_to_check):
        # go over each letter in the word
        # identify if the letter is a capital letter
        # write somewhere the index of the capital letter
        if letter in ascii_uppercase:
            capital_indexes.append(index)
    return capital_indexes
"""

# PROBLEM5
"""
# The goal of this challenge is to analyze a string to check if it contains
# two of the same letter in a row. For example, the string "hello" has l twice
# in a row, while the string "nono" does not have two identical letters in a row.

# Define a function named double_letters that takes a single parameter.
# The parameter is a string. Your function must return True if there are
# two identical letters in a row in the string, and False otherwise.


def check_double_letters(word_to_check: str):
    # go through each letter in the word
    # see if the letter you're on matches the one in front/behind
    # if that ever happens, write true off to the side
    current_letter = []
    for index, letter in enumerate(word_to_check):
        current_letter.append(letter)
        if index < 0:
            if letter == current_letter[index-1]:
                return True
    return False


def check_double_letters_v2(word_to_check: str):
    past_letter = ""
    for index, letter in enumerate(word_to_check):
        if index > 0:
            past_letter = word_to_check[index-1]
            if past_letter == letter:
                return True
    return False
"""

# IF STATEMENTS CAN BE USED TO STOP THE CODE FROM 
# RUNNING SOMETHING UNTIL A CERTAIN POINT OR CONDITION IS MET

# PROBLEM6
"""
# take a list of lists and conver it to a single dimensional list
# aka [[1,2],[3,4]] => [1,2,3,4]

def list_abtstractor(nested_num_list):
    # nested_num_list = [[1,2],[3,4]] # solid name!
    for num_list in nested_num_list[1:]: # slicing first number is inclusive
        for num in num_list:
            nested_num_list[0].append(num)
    return nested_num_list[0]
# No need to enumerate here because the index we're modifying is the same every time
"""

# PROBLEM7
"""
# write a function that takes a string and adds a dot between each letter
# for example test => t.e.s.t.
def add_periods(some_string):
    empty_string = ""
    for letter in some_string:
        # append maybe?
        # maybe at the index+1 add a period for each character in the string
        empty_string += (letter + ".")
    return empty_string
# print(add_periods("hello"))
"""

# PROBLEM8
"""
# palindromes; if the word is the same forward and backwards, return true
# if the word is not the same forwards and backwards, return false
def check_palindrome(some_string):
    # have to use a for loop/cannot use reversed function

    if some_string[0] == some_string[-1]:
        string_to_compare = "" #dog => add item at 2nd index to empty string, then 1st, then 0
        some_string_final_index = len(some_string) - 1
        for index in range(some_string_final_index, 0, -1): # stop is not inclusive
            string_to_compare += some_string[index]
        string_to_compare += some_string[0]
        if string_to_compare == some_string:
            return True
    return False
"""

# HOW TO MAKE EMPTY VARIABLES FOR EACH TYPE
# empty_num = 0
# empty_string = ""
# empty_list = []

# PROBLEM9
"""
# count syllables if you are given a word that already has the syllables seperated by
# a hyphen. For example; if the word looks like "hel-lo" the function should return 2
def check_syllables(some_string: str) -> int:
    hyphens = 0
    # check if there is a hyphen in the word
    if "-" in some_string:
        # go over each letter in the word
        for letter in some_string:
            # if it's a hyphen, 
            if letter == "-":
                # hyphens variable += 1
                hyphens += 1
        # return hyphens variable
        return hyphens
    return 0            
    # if there isn't, return 0
"""

# PROBLEM10
"""
# accept input from a user
# in a list from 1-10, add that number the user typed to each in the list
# do that again, however many times the user typed in

# example VVVVVV
# [1,2,3,4,5,6,7,8,9,10]
# user types 2
# add 2 to each number in the list, 2 times
# expected output => [5,6,7,8,9,10,11,12,13,14]

# must use a while loop and a for loop

num_list = [1,2,3,4,5,6,7,8,9,10]
user_input = int(input()) # 2
control_num = 0
while user_input > control_num: # this controls how many times we do the addition
    control_num += 1
    for index in range(10):
        num_list[index] += user_input
print(num_list)
"""

# USE RANGE WHEN YOU HAVE A FIXED NUMBER OF THINGS TO LOOP OVER

# USE THE ITERABLE ITSELF WHEN IT'S NOT A FIXED LENGTH EACH TIME YOU RUN IT
# OTHERWISE, USE THE ITERABLE ITSELF WHEN YOU NEED TO ACCESS 
# THE ITEMS WITHIN THE ITERABLE

# USE THE ITERABLE PLUS ENUMERATE WHEN YOU NEED THE ITEMS AND THE INDEX

# WHILE LOOPS ARE THE EXACT SAME THING AS A FOR LOOP UNDER THE HOOD
"""
# adding "hello" to a list a certain number of times
# first, here's how we'd do it in a while loop
empty_list = []
start = 0
stop = 5
while start < stop:
    empty_list.append("hello")
    start += 1

# here's how we achieve the exact same thing by using a for loop
for num in range(5):
    empty_list.append("hello")

# all the following code can be done in a while loop since they both 
# function the same. for loops are preferred in these cases because
# they do what a while loop does with less lines
user_given_numb = int(input("enter a whole number: "))
for numb in range(1, 11):
    print(numb * user_given_numb)
"""

# PROBLEM11
"""
numbers_in_list = [12, 75, 150, 180, 145, 525, 50]
for num in numbers_in_list:
    if num > 150 and num <= 500:
        print("skip")
        continue
    if num > 500:
        print("break")
        break
    if num % 5 == 0:
        print(num)
"""

# PROBLEM12
"""
# Calculate the sum of all numbers from 1 to a given number
# Write a program to accept a number from a user 
# and calculate the sum of all numbers from 1 to a given number
# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

user_input = int(input())
empty_list = []
for num in range(1, user_input+1):
    # append num to the list and add it
    empty_list.append(num)
# empty list => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_empty_list = []
empty_num = 0
for num in empty_list:
    empty_num += num
    if num  < user_input-1:
        num += empty_list[num + 1]
        new_empty_list.append(num)
# new_empty_list => [3, 5, 7, 9, 11, 13, 15, 17, 19] !!!!
"""

# PROBLEM13
"""
user_input = int(input()) + 1
final_result = 0
for num in range(1, user_input):
    final_result += num
print(final_result)
"""

# PROBLEM14
"""
user_given_numb = int(input("enter a whole number: ")) + 1

for outer_num in range(1, user_given_numb):
    for inner_num in range(1, outer_num + 1):
        
        # THIS IS THE FIRST WAY THIS COULD BE SOLVED
        # if inner_num < outer_num:
        #     print("*", end=" ")
        # elif inner_num == outer_num:
        #     print("*")
        
        # THIS IS THE SECOND, MORE EFFECTIVE WAY TO SOLVE THIS
        print("*", end=" ")
    print("")

# User Input == 5
# *
# **
# ***
# ****
# *****
"""

# RANGE TIPS/THINGS TO REMEMBER
# range(5) => stops at 4, starts at 0
# range always starts at 0 unless you say otherwise
# range(1, 6) stops at 5, starts at 1

# PROBLEM15
"""
# Iterate string in reverse order
# if the user types in "hello" print out "o l l e h"

# get a word
# make a empty string to store n new word
# go overletters in word

forward_string = input("enter a word: ")
forward_string = reversed(forward_string)

reversed_string = ""
for letter in forward_string:
    print(letter + " ", end=" ")
"""

# PROBLEM16
"""
test_dict = {"cheese": "doodle",
             "bad": "dog",
             "good": "day",
             "chicken": "salad"}
for key, value in test_dict.items():
    print(key + " === " + value)
"""

# COUNT vs LEN FUNCTION NOTES/THINGS TO REMEMBER
# count is how many of X exists in Y (aka how many "c"'s are in a string/list/dict) 
# counts ONE thing

# len is how many items are in the string/list/dict in total
# len counts EVERYTHING
# len always returns 1 more than the last index in the item
# if the last index is 5, len will return 6
# reason is because indexes start at 0, len will count starting at 1

# PROBLEM17
"""
# same instructions as problem 15, just can't use "reversed"

forward_string = input("enter a word: ") 
for index in range(len(forward_string) - 1, -1, -1): 
    # start is inclusive, stop is NOT inclusive
    print(forward_string[index], end=" ")
"""

# FINAL NOTES
# ask yourself what is the result of coding this line?
# if that result is what you wanted, leave it
# otherwise, try something else
# if you don't know what the result of the current line is, 
# run it before you carry on