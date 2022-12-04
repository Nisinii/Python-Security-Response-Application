import Customer as cust
import Researcher as re

#Creating the login menu

def menu():
    print("------------------------------ LOGIN ------------------------------")
    print("Login As... \n01. Customer \n02. Researcher \n03. Exit application")
    login = int(input("Enter your login option (1, 2 or 3) : "))
    print("-------------------------------------------------------------------")

    if login == 1:
        cust.customer()
        print("\n\n\n-------------------------------------------------------------------")
        menu()

    elif login == 2:
        re.researcher()
        print("\n\n\n-------------------------------------------------------------------")
        menu()

    elif login == 3:
        print("\n\n-------------------------------------------------------------------")
        print("Thank you for using our application!")         
        print("-------------------------------------------------------------------")

    else:
        print("\nInvalid output!")
        
menu()
