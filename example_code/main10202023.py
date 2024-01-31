# get name
name = input("what is your name?: ")
# funtion to check namw


def name1():
    if name == " ":  # checks if name input is not a string
        print("you did not enter your name")
    elif int(name):
        print("thats a number ")
    else:  # if name input is a string
        print(f"welcome back {name}")
# check name
def name():
    try:  # checks if name is a int
        name = int(name)
        print("That is not a name, that is a number.")
    except:  # if not int run name1()
        name1()

# open with welcom back user name
