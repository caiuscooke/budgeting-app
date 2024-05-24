import os

cwd = os.path.join(os.getcwd(), "budgeting-app")

TRANSACTION_FILE_NAME = os.path.join(cwd, "transactions.txt")
PAYCHECK_FILE_NAME = os.path.join(cwd, "paychecks.txt")
BALANCE_FILE_NAME = os.path.join(cwd, "balances.txt")
LOGIN_FILE_NAME = os.path.join(cwd, "login.txt")


def read_file_contents(file_name: str) -> list:
    """
    This function opens a txt file, reads the contents, and returns
    each line in a list
    """
    with open(file_name, "r") as file:
        file_contents = file.readlines()
    return file_contents
