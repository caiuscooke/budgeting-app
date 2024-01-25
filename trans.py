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
    transaction_date = input()
    with open('trans.txt', 'r') as file:
        transactions = file.readlines()
        for each in transactions:
            line_split = each.split()
            date = line_split[3]
            if transaction_date == date:
                print(each)


display_transactions()
