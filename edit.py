def get_edit_info():
    from datetime import datetime
    from get_input import convert_input_to_datetime
    from file_manipulation import get_txt_lines
    print("do you want to edit one  or multiple transactions")
    print("What do you want to edit in transactions?: date, category, amount, time")
    user_input_as_date = input()
    user_input_as_date = convert_input_to_datetime()
    transactions = get_txt_lines(user_input_as_date)
    edit_item_list = transactions
    for  in edit_item_list:

