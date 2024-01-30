class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save(self):
        with open("login.txt", "a") as file:
            file.write(
                f"\n{self.username} {self.password}")


username = input("Type in a username")
new_user = Login("caius_cooke", "12345678")
new_user.save()
