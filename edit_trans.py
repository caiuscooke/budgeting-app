# can we edit the del function to make this

# import date time
from datetime import datetime
# import convert_input_to_daterime
from get_input import convert_input_to_daterime
# import the lines from the textfile
from file_manipulation import get_txt_lines

#maybe add a while loop  to keep it going unless the user says no to editing or quits 

# are you editing one or more transactions.
print("do you want to edit one or multiple transactions?")
# get user input for date wants to edit
user_input_as_date = convert_input_to_daterime
# get transaction/s that user wants to edit
transactions = get_txt_lines(user_input_as_date)
print(f"is this the {transactions}transaction tou want to edit ")
#if transaction == correct transaction 
print("What do you want to edit in transactions?:  date , category, amount, time, product?")
# what do you want to edit the, date, category
# amount, time, product
#ui for choice of edits they wanna make 
edits=input("")
#?edit with a for loop each of the 0-4 indexs in the list categories 
for edits in transactions:

       if "procuct"== edits: 
                #if product
        #print(f"what do you want to turn {edit}")
        #ui the new edit1 
        edit1= input("what is the new product?: ")
        #print(f"are you sure you want to change {edit} to {edit1}")
        #"y" to append or write edit1 to txt file and 
        #update txt file with edit1  
        #print ("would you like to change anytthing else in this transaction?")
        #"n" ui enter new product 
        elif transactions[0]== indexs:
     #if  date 
        #ui the new date 
        #are you sure you want to change date to date 1
        #"y" to append 
        #"n" ui enter new date 
        #would you like to change anytthing else in this transaction .

    elif transactions[1]== indexs:
    #elif category 
        #ui the new category 
        #are you sure you want to change category to catefory 1
        #"y" to append 
        #"n" ui enter new category
        #would you like to change anytthing else in this transaction .
    elif transactions[2]== indexs:
        #elif amount
        #ui the new amount 
        #are you sure you want to change amount to amount 1
        #"y" to append 
        #"n" enter new amount 
        #would you like to change anytthing else in this transaction . 
    elif "time"== transactions[3]:
        #elif time
        #ui the new time 
        #are you sure you want to change time to time 1
        #"y" to append 
        #"n" ui enter new time 
        #would you like to change anytthing else in this transaction .
 


        #print ("would you like to edit another transaction.")