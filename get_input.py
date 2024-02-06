from datetime import datetime


def check_user_input(input_field_name: str):

    number_input = input(f"{input_field_name}: ")
    input_is_numbers = False

    while not input_is_numbers:
        try:
            int(number_input)
            input_is_numbers = True
        except:
            print("Make sure you only type numbers.")
            number_input = input(f"{input_field_name}: ")
            continue

        if len(number_input) != 2:
            print(f"Enter two digits for the {input_field_name}.")
            number_input = input(f"{input_field_name}: ")
            input_is_numbers = False
            continue

        date_num_in_range = int(number_input) < 1 or int(number_input) > 31
        if input_field_name == "Day" and date_num_in_range:
            print("Type a real day.")
            number_input = input(f"{input_field_name}: ")
            input_is_numbers = False
            continue

        date_num_in_range = int(number_input) < 1 or int(number_input) > 12
        if input_field_name == "Month" and date_num_in_range:
            print("Type a real month.")
            number_input = input(f"{input_field_name}: ")
            input_is_numbers = False
            continue

    return number_input


def convert_input_to_datetime():

    print("Input two digits for the day, month, and year.")
    print("Ex) 07 22 20 for July 22nd, 2000")

    day = check_user_input("Day")
    month = check_user_input("Month")
    year = check_user_input("Year")

    date_string = f"{month}:{day}:{year}"
    user_input_as_date = datetime.strptime(date_string, "%m:%d:%y")

    return user_input_as_date
