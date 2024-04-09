from datetime import datetime


def get_txt_lines(user_input_as_date: datetime):
    with open('trans.txt', 'r') as file:
        transactions = file.readlines()

        transaction_results = []
        for index, transaction in enumerate(transactions):
            line_split = transaction.split()
            date = line_split[3]  # string date from the txt file
            txt_file_as_date = datetime.strptime(date, "%Y-%m-%d")

            if user_input_as_date == txt_file_as_date:
                transaction_results.append(f"{transaction} {index}")

        return transaction_results
