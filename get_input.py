from datetime import datetime, time, date


def check_user_input(input_field_name: str): # define a function with a str paramater

    number_input = input(f"{input_field_name}: ") # ask user for a number as input
    input_is_numbers = False # set a variable controlling if the input is a number or not to false

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
    print("Ex) 07 22 20 for July 22nd, 2020")

    month = check_user_input("Month")
    day = check_user_input("Day")
    year = check_user_input("Year")

    date_string = f"{month}:{day}:{year}"
    user_input_as_date = datetime.strptime(date_string, "%m:%d:%y")

    return user_input_as_date


def get_category():

    category_options = (
        "Groceries", "Commuting", "Entertainment", "Dining",
        "Home Improvement", "Self-Care", "Work Related Expenses",
        "Cost of Living Bills", "Subscriptions"
    )

    print("Select a category that fits your transaction:")
    for index, category in enumerate(category_options):
        print(f"{index+1}) {category}")

    selected_category = input("Enter a number:  (1/9) ")
    selected_index = int(selected_category) - 1

    return category_options[selected_index].lower()


def get_amount():
    amount = input("Enter the $ amount: ")  # "4000"
    amount_float = float(amount)  # -> int 4000
    amount = "{:.2f}".format(amount_float)  # -> str "4000.00"
    return amount


def get_time():
    hours = input("Enter the hours: ")
    hours_int = int(hours)

    minutes = input("Enter the minutes: ")
    minutes_int = int(minutes)

    time_object = time(hours_int, minutes_int)
    return str(time_object)


def get_date():
    date_object = convert_input_to_datetime().date()

    return str(date_object)
