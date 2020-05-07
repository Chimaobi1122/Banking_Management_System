import json
import sys
import random 
import os
from datetime import datetime

customer_file="customers.txt"
staff_file = "staffs.txt"
customer_data=[]
user_session = "user_session.txt"



#staff data 
data = {}
data["staff"] = []
data["staff"].append({
    "Fullname": "Onuh Chuks",
    "Username": "chuks",
    "Password": "1234",
    "Email": "chuksonuh@email.com"
})
data["staff"].append({
    "fullname": "James John",
    "username": "James",
    "password": "1234",
    "email": "jamesjohn@email.com"
})
#A function to write data to a file 
def write_data(file_name, file_contents):
    with open(file_name, "w") as staff_file:
        json.dump(file_contents, staff_file)


#checks the user login from file before granting access
def check_login():    
    with open('staffs.txt') as json_file:
	
        data = json.load(json_file)
        global Username
        Username = input("Username: ")
        Password =input("Password: ")
        for foo in data['staff']:
            if foo["Username"] == Username and foo["Password"] == Password:
                x = foo["Username"] 
                y = foo["Password"]
                x == y  is True
                #Creates a login session for a staff and saves it to session.txt
                login_time= Username +" "+ "signed-in at " + str(datetime.now())
                write_data(user_session, login_time) 
                print (f"Welcome {Username}")
                staff_permissions()
                break
            else:
                print("Invalid username or password!!!")
                check_login()

#Main menu for before login 
def main():
    print("""	
	1. Staff Login
	2  Exit
	""")
    choice = input("Select an option: ")
    
    if choice == "2":
        sys.exit()
        
    elif choice == "1":
        print("Enter login details: ")
        check_login()
        
    else:
        print("Enter a valid input!!!")
        main()
    # except:
        #     ("Enter a number 1 or 2")
        #     main()
#After the user logs in he can use any of the features below 
def staff_permissions():
    print("""	
	1. Create new bank account
	2  Check account details
	3. Logout
	""")
    staff_selection=input()
    if staff_selection == "1":
        print ("Enter the customer's information ")
        account_name = input("Account full name: ")
        starting_balance = input("starting Balance: ")
        account_type= input("Account Type: ")
        email= input("Customer's email: ")
        #Generate a random account Number 
        account_number = random.randint (1000000000, 9999999999)
        #append customer data to a list 
        customer_data.append([account_name, starting_balance, account_type, email, account_number])
        print(customer_data)
        #write customer data to file
        write_data(customer_file, customer_data)
        print("Account successfully created!!!")
        print (f"Your new account number is {account_number}")
        staff_permissions()
#feature to check the account number from  file 
    elif staff_selection == "2":
        check_account = int(input("Enter your account number: "))
        print (f"Your account number is {check_account}")
        with open(customer_file) as json_file:
            data = json.load(json_file)
            if int(data[0][4]) == check_account:
                print (f"Your Account balance is {data[0][1]}")
                staff_permissions()
            else:
                print("Account not found")
                staff_permissions()
#Log out and return to the main menu 
    elif staff_selection == "3":
        logout_time= Username +" "+ "signed-out at " + str(datetime.now())
        write_data(user_session, logout_time)
        print(logout_time) 
        os.remove("user_session.txt")
        main()
    else:
        ("Invalid input!!!")
        staff_permissions()

write_data(staff_file, data)
main()
check_login()



    