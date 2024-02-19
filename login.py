from string import ascii_uppercase

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        with open("login.txt", "a") as file:
            file.write(
                f"\n{self.username} {self.password}")

def create_user():
    # user has only seen "do you have an account"
    # user has typed n
    # now we're in this function
    
    # ask for username
    # open the text file
    # read the textfile into a list (aka use readlines())
        # for each item in that list
            # if username in each
                # notify user that name is already taken
                # recursively call the create_user function
    # list of unaccepted characters
    # print a statement of the requirements (one capital, one number, one special character)
    # print unacceptable characters
    # while True
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
    # confirm username and password to user
    # create an instance of the User class
    # call the save function on the new instance
    # return True
    pass


