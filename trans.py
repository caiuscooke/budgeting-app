from datetime import datetime


class Transaction:
    def __init__(self, category: str, amount: float, time: str, date: str, product: list):
        self.category = category
        self.amount = amount
        self.time = time
        self.date = date
        self.product = product

    # create a txt:
    def save(self):
        with open("trans.txt", "a") as file:
            file.write(
                f"\n{self.category} {self.amount} {self.time} {self.date} {self.product}")


# create a way to view the trans text file
def view():
    with open("trans.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line)


def display_transactions():
    print("Input two digits for the day, month, and year.")
    print("Ex) 07 22 20 for July 22nd, 2000")

    """
    Find each line that needs to change. Aka line 37
    will need the changes in the comments.
    """
    # FROM HERE
    # variable name has to change and input string has to change
    day = input("Day: ")
    while True:
        try:
            int(day)
            break
        except:
            print("Make sure you only type numbers.")
            day = input("Day: ")

    while len(day) != 2:
        print("Enter two digits for the day.")
        day = input("Day: ")
    # TO HERE

    month = input("Month: ")
    while len(month) != 2:
        print("Enter two digits for the month.")
        month = input("Month: ")

    year = input("Year: ")
    while len(year) != 2:
        print("Enter two digits for the year.")
        year = input("Year: ")

    date_string = f"{day}:{month}:{year}"
    user_input_as_date = datetime.strptime(date_string, "%m:%d:%y")

    with open('trans.txt', 'r') as file:
        transactions = file.readlines()
        for transaction in transactions:
            line_split = transaction.split()
            date = line_split[3]  # string date from the txt file
            txt_file_as_date = datetime.strptime(date, "%m:%d:%Y")

            if user_input_as_date == txt_file_as_date:
                print(transaction)


display_transactions()
