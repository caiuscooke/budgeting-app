age = 55
# storing an age
colors_str = "red blue yellow"


def get_number_of_colors(some_str: str) -> int:
    colors_list = some_str.split()
    return len(colors_list) + 1


# get\retreive
# check
# eval
some_string = "h e l l o"
empty_list = []
for each in some_string:
    empty_list.append(each)

empty_string = ""
for each in some_string:
    empty_string += each
