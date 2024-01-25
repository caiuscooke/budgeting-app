class trans:
    def __init__(self, category: str, amount: float, time: str, date: str):
        self.category = category
        self.amount = amount
        self.time = time
        self.date = date
# create a txt:

    def save(self):
        with open("trans.txt", "a") as file:
            file.write(
                f"\n{self.category} {self.amount} {self.time} {self.date}")
# creat a way to view the trans text file

    def view():
        with open("trans.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                print(line)
