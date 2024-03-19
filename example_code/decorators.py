
def add_then_subtract(num1, num2, num3):
    sum = num1 + num2
    answer = sum - num3    

def add_then_multiply(num1, num2, num3):
    sum = num1 + num2
    answer = sum * num3

def add_then_divide(num1, num2, num3):
    sum = num1 + num2
    answer = sum / num3

def add_then_operation(num1, num2, num3, operation):
    sum = num1 + num2
    if operation == "-":
        answer = sum - num3
    elif operation == "*":
        answer = sum * num3
    elif operation == "/":
        answer = sum / num3

def add_first_two_parameters(func):
    def wrapper(*args, **kwargs):
        if len(args) >= 2:
            # Sum the first two parameters
            sum_of_first_two = args[0] + args[1]

            # Call the original function with the sum and the rest of the arguments
            result = func(sum_of_first_two, *args[2:], **kwargs)

            return result
        else:
            raise ValueError("Not enough arguments provided.")

    return wrapper


@add_first_two_parameters
def multiply_by_third_param(sum_of_first_two, third_param):
    return sum_of_first_two * third_param

@add_first_two_parameters
def divide_by_third_param(sum_of_first_two, third_param):
    return sum_of_first_two / third_param

# Example usage
result_multiply = multiply_by_third_param(3, 4, 5)  # (3 + 4) * 5 = 35
result_divide = divide_by_third_param(3, 4, 2)  # (3 + 4) / 2 = 3.5

print("Result of multiply:", result_multiply)
print("Result of divide:", result_divide)
