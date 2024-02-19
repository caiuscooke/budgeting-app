import trans


def main():
    print("Welcome to the budget app")

    have_account = input("Do you have an account? [y/n]: ")
    if have_account.lower() == "y":
        # go to the login function
        pass
    elif have_account.lower() == "n":
        # go to the create user function
        pass
    else:
        # handle other input errors here
        pass

    options = ["Edit", "View", "Add",
               "Delete", "View All", "Delete All"]
    option_map = {
        options[0]: "xxxxxxxx",
        options[1]: "view",
        options[2]: "add_transaction",
    }

    user_logged_in = True  # placeholder
    while user_logged_in:
        print("Main Menu")
        for index, each in enumerate(options):
            print(f"{index+1}) {each}")
        print("type a number to select an option")
        choice = input()
        for index, option in enumerate(options):
            if (int(choice) - 1) == index:
                function_attribute = getattr(trans, option_map.get(option))
                function_attribute()


main()
