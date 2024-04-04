# ran_list = [["word1", "word2", "word3"], ["word4", "word5", "word6"]]
# for list in ran_list:
#     for word in list:
#         print(word)
#     print(list)


# num_list = [[1, 1, 1], [2, 1, 3]]
# for list in num_list:
#     multiplyer = sum(list)
#     for index, num in enumerate(list):
#         num *= multiplyer
#         print(num * multiplyer) 
#         list[index] *= multiplyer
#     print(list)


num_list = [[1, 1, 1], [2, 1, 3]]
for list in num_list:
    total = 0
    for num in range(0, len(list)):
        total = total + list[num]

    for index, num in enumerate(list):
        list[index] *= total
    print(list)

# list, str, int, float, bool, etc.