def first_function():
    return True

def new_function():
    user_input = int(input())
    if user_input == 1:
        return first_function()

    elif user_input == 2:
        return True

boolean_value = new_function()
print(boolean_value)