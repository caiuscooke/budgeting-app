class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        with open("login.txt", "a") as file:
            file.write(
                f"\n{self.username} {self.password}")
