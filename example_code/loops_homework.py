# make a for loop that adds each letter of the a word to a list
# user_input = input()
# characters_list = []

# for each in user_input:
#     characters_list.append(each)
# print(characters_list)

# make a for loop that checks if a letter in a word occurs 2 or more times
# user_input = input()
# repeating_letters = []
# for each in user_input:
#     repeat_count = user_input.count(each)
#     if repeat_count > 1:
#         repeating_letters.append(f"{each}{repeat_count}")

# repeating_letters_set = set(repeating_letters)
# print(repeating_letters_set)

# printed_letter = []
# for each in repeating_letters:
#     if each not in printed_letter:
#         printed_letter.append(each)
#         print(each)

# cheese => [e3, e3, e3] => set(e3)

# make a for loop that adds a random word to each entry in a list
# ["hello", "world"] -> ["hello randomword1", "world randomword2"]
import random
random_words_list = ["cheese", "doodle", "cash", "code", "learn"] # words_list => random_words_list
test_list = ["hello", "word"]

for index, word in enumerate(test_list): # change test => word
    random_word = random.choice(random_words_list) # added this to the loop scope
    test_list[index] += random_word # append(random_word) => test_list[index] += random_word
    
print(test_list) # took this from the loops scope => outside of the loop

# anytime you want to modify the current instance in the loop, 
# use "for index, each in enumerate(iterable):" 
# (each is the individual item, iterable is the list\string)
# in the loop itself, change the current instance with "iterable[index] = new_item"

from string import ascii_uppercase
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

# The goal of this challenge is to analyze a string to check if it contains
# two of the same letter in a row. For example, the string "eello" has l twice
# in a row, while the string "nono" does not have two identical letters in a row.

# Define a function named double_letters that takes a single parameter. 
# The parameter is a string. Your function must return True if there are 
# two identical letters in a row in the string, and False otherwise.

def check_double_letters(word_to_check: str):
    # go through each letter in the word
    # see if the letter you're on matches the one in front\behind
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

# if statements can be used to stop the code from running something until a certain point
