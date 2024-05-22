from string import ascii_lowercase, ascii_uppercase

from core import LOGIN_FILE_NAME, read_file_contents


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        with open("login.txt", "a") as file:
            # apply password hashing here
            # hashed = self.password
            file.write(
                f"\n{self.username} {self.password}")


def create_user():
    # user has only seen "do you have an account"
    # user has typed n
    # now we're in this function

    # ask for username
    print("Enter your username")
    username = input()  # asdf;lkajsdf
    if " " in username:
        return create_user()

    lines = read_file_contents(LOGIN_FILE_NAME)

    for each in lines:
        # if username in each
        if username in each:
            # notify user that name is already taken
            print("That username is already taken")
            # recursively call the create_user function
            return create_user()

    # list of accepted characters
    accepted_char_list = ["!", "#", "%", "&", "?", "@", "￥", "$"]
    acceptable_num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    # print a statement of the requirements (one capital, one number, one special character)
    print(
        "Password must have at least one lowercase, "
        + "one uppercase, one special character, and one number"
    )
    # print acceptable characters
    accepted_char_str = " ".join(accepted_char_list)
    print(f"The accepted characters are {accepted_char_str}")
    # while True
    while True:
        # ask for password
        first_password = input("Enter your password: ")
        # for each in password
        has_capital, has_symbol, has_number, has_lower = False, False, False, False

        for each in first_password:  # 1L7xvb#09!

            # if each is in a list of capital letters
            if each in ascii_uppercase:
                # set a variable called has_capital to true
                has_capital = True
            # elif each is in a list of acceptable symbols
            elif each in accepted_char_list:
                # set a variable called has_symbol to true
                has_symbol = True
            # elif each is 1 - 0
            elif each in acceptable_num_list:
                # set a variable called has_number to true
                has_number = True
            elif each in ascii_lowercase:
                has_lower = True
            # else
            else:
                # tell the user that the character they inputed was unacceptable
                print("You have an unaccepted character in your chosen password")
                break
        # ask for password again
        confirmation_password = input("Enter your password again: ")
        passwords_match = confirmation_password == first_password
        password_len_ok = len(first_password) >= 8
        password_ok = (has_capital
                       and has_symbol
                       and has_number
                       and has_lower
                       and password_len_ok
                       and passwords_match)
        if password_ok:
            # break
            break
        elif not password_ok:
            print("password NOT ok!")
            continue
    print("password OK!")
    # confirm username and password to user
    # create an instance of the User class
    # call the save function on the new instance
    # return True
    pass


create_user()
