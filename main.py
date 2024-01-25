<<<<<<< HEAD
from trans import trans
view = 1
add = 2
edit = 3
delete = 4
print("welcome to the budgeting app.")
option = int(input("type 1 for view 2 for add 3 for edit 4 for delete."))
if option == view:
    trans.view()
elif option == add:
    category = input("category of purchase ")
    amount = float(input("amount of purchase "))
    time = input("time of purchase ")
    date = input("date of purchase ")

    transaction = trans(category, amount, time, date)
    transaction.save()

# elif option== edit:#
=======
file = open("helloworld.txt", "w")
file.write("10+10")
file.close()

with open("helloworld.txt", "w") as file:
    file.write("hello world")
>>>>>>> c572937650c21093efc24632e335bfa854ce3335
