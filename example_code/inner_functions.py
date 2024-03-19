def parent(number: int):
    print("Printing from parent()")
    
    def first_child():
        print("Printing from first_child()")

    def second_child():
        print("Printing from second_child()")
    
    if number == 1:
        first_child()
    second_child()

parent(1)


def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator
def say_whee():
    print("Whee!")

say_whee()

@decorator
def say_hello():
    print("Hello!")

say_hello()

@decorator
def say_bye():
    print("Bye!")

say_bye()