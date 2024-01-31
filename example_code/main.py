file = open("helloworld.txt", "w")
file.write("10+10")
file.close()

with open("helloworld.txt", "w") as file:
    file.write("hello world")
