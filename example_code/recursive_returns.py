def recursive_function(number: int) -> bool:
    if number < 5:
        return True
    return recursive_function(number - 1)

# print(recursive_function(5))

# list_of_words = ["word1", "word2", "word3", "word4"]

# while True:
#     for each in list_of_words:
#         print(each)
#     user_choice = input("Would you like to see it again? y/n: ")
#     if user_choice == "y":
#         continue
#     else:
#         break

# def print_list(list_of_words):
#     for each in list_of_words:
#         print(each)
#     user_choice = input("Would you like to see it again? y/n: ")
#     if user_choice == "y":
#         print_list(list_of_words)
#     else:
#         return
    
# print_list(list_of_words)

# example:
# x = 10
# return should be the value of 1 * 2 * 3 * ... * 10
def factorial(x):
    if x <= 1:
        return 1
    else:
        return (x * factorial(x - 1))

print(factorial(5))