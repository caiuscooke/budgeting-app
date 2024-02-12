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
        for index, each in enumerate(options):
            print(f"{index+1}) {each}")
        print("type a number to select an option")
        choice = input()
        if choice == "2":
            trans.view()
        elif choice == "4":
            trans.delete_transaction()


main()
