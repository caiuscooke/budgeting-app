# make a for loop that adds each letter of the a word to a list
# ui = input("type a word?: ")
# al = []
# for each in ui:
#     al = [each]
# print(al)

# make a for loop that checks if a letter in a word occurs 2 or more times
# test word
# ui = "cheese"
# # for each letter in test word
# for each in ui:
#     if ui.count(each) > 1:
#         print("that letter repeats?")
# make a for loop that adds a random word to each entry in a list
# ["hello", "world"] -> ["hello randomword1", "world randomword2"]
import random
words_list = ["cheese", "doodle", "cash", "code", "learn"]
test_list = ["hello", "word"]
random_word = random.choice(words_list)
for test in test_list:
    test_list.append(random_word)
    print(test_list)
