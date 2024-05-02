from get_input import get_amount, get_time, get_date

class Paycheck:
    def __init__(self, amount: str, time: str, date: str):
        self.amount = amount
        self.time = time
        self.date = date

    def save(self):
        with open("paychecks.txt", "a") as file:
            file.write(
                f"\n{self.amount} {self.time} {self.date}")


def add_paycheck():

    print("Type in the information based on the prompt")
    
    amount = get_amount()
    time = get_time()
    date = get_date()

    paycheck_information = f"{amount} {time} {date}"
    is_correct = input(f"Is {paycheck_information} correct? [y/n]: ")

    if is_correct.lower() == "y":
        new_paycheck = Paycheck(
            amount, time, date
        )
        new_paycheck.save()
        print("The paycheck has been saved.")
        add_more = input("Would you like to add another paycheck? [y/n]: ")
        if add_more.lower() == "y":
            add_paycheck()
    elif is_correct.lower() == "n":
        add_paycheck()