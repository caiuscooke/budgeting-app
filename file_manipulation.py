from datetime import datetime


def get_txt_lines(user_input_as_date: datetime):
    with open('trans.txt', 'r') as file:
        transactions = file.readlines()

        transaction_results = []
        for transaction in transactions:
            line_split = transaction.split()
            date = line_split[3]  # string date from the txt file
            txt_file_as_date = datetime.strptime(date, "%m:%d:%Y")

            if user_input_as_date == txt_file_as_date:
                transaction_results.append(transaction)

        return transaction_results
