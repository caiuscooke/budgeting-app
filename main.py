import trans


def main():
    print("Welcome to the budget app")
    have_account = input("Do you have an account? y/n: ")
    if have_account.lower() == "y":  # place loop here
        # go to the login function
        pass
    else:
        # go to the create user function
        pass

    user_logged_in = True  # placeholder

    if user_logged_in:
        print("Welcome back")
        options = ["Edit", "View", "Add", "Delete", "View All", "Delete All"]
        option_map = {
            options[0]: "xxxxxxxx",
            options[1]: "view",
            options[2]: "Transaction",
        }
        for index, each in enumerate(options):
            print(f"{index+1}) {each}")
        print("type a number to select an option")
        choice = input()
        # replace with the following pseudo
        # loop through options
        # if choice as an int minus 1 equals the current index in the loop
        # get the attribute from trans module for the appropriate choice
        # call the attribute
        for index, option in enumerate(options):
            if (int(choice) - 1) == index:
                function_attribute = getattr(trans, option_map.get(option))
                function_attribute()


main()
