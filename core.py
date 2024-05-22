TRANSACTION_FILE_NAME = "transactions.txt"
PAYCHECK_FILE_NAME = "paychecks.txt"
BALANCE_FILE_NAME = "balances.txt"
LOGIN_FILE_NAME = "login.txt"


def read_file_contents(file_name: str) -> list:
    """
    This function opens a txt file, reads the contents, and returns
    each line in a list
    """
    with open(file_name, "r") as file:
        file_contents = file.readlines()
    return file_contents
