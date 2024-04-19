sandwich_ingredients = ["bread", "cheese", "ham", "mayo", "bread"]

# for ingredient in sandwich_ingredients:
#     print(ingredient)

print(*sandwich_ingredients, sep="\n")

def find_sum(list_of_items_to_be_added=[1, 5], *args, **kwargs):

    if kwargs.get("color"):
        print(kwargs.get("color"))

    if "*" in args: 
        print(list_of_items_to_be_added)
    elif len(args) > 1: 
        print(list_of_items_to_be_added + list(args))
    else:
        print(sum(list_of_items_to_be_added))


find_sum()