from string import ascii_uppercase, ascii_lowercase


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
    username = input() # asdf;lkajsdf
    if " " in username:
        return create_user()
    
    # open the text file
<<<<<<< HEAD
    # read the textfile into a list (aka use readlines())
    # for each item in that list
    # if username in each
    # notify user that name is already taken
    # recursively call the create_user function
    # list of unaccepted characters
=======
    with open("login.txt", "r") as file:
        # read the textfile into a list (aka use readlines())
        lines = file.readlines() # ["caiuscooke al;skdjf908234jlasdf"]
        # for each item in that list
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
>>>>>>> 04a842dae3ce3e3b91b598222bb02683c47a6ca2
    # print a statement of the requirements (one capital, one number, one special character)
    print(
        "Password must have at least one lowercase, "
        + "one uppercase, one special character, and one number"
    )
    # print acceptable characters
    accepted_char_str = " ".join(accepted_char_list)
    print(f"The accepted characters are {accepted_char_str}")
    # while True
<<<<<<< HEAD
    # ask for password
    # ask for password again
    # for each in password
    # if each in unaccepted characters
    # print that the user has chosen an unacceptable character
    # continue
    # if each is in a list of capital letters
    # set a variable called has_capital to true
    # if each is in a list of acceptable symbols
    # set a variable called has_symbol to true
    # if each is 1 - 0
    # set a variable called has_number to true
    # if confirmation matches and (has_capital, has_symbol, and has_number is true)
    # break
=======
    while True:
        # ask for password
        first_password = input("Enter your password: ")
        # ask for password again
        confirmation_password = input("Enter your password again: ")
        # for each in password
        has_capital, has_symbol, has_number = False

        for each in first_password: # 1L7xvb#09!
            
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
                continue
            # else
            else:
                # tell the user that the character they inputed was unacceptable
                print("You have an unaccepted character in your chosen password")
                # continue
                continue
            
        # if confirmation matches and (has_capital, has_symbol, and has_number is true)
            # break 
>>>>>>> 04a842dae3ce3e3b91b598222bb02683c47a6ca2
    # confirm username and password to user
    # create an instance of the User class
    # call the save function on the new instance
    # return True
    pass
