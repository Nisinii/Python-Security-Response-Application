import re   
  
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  

def customer():

    print("\nWelcome to Security response team!\nPlease enter the following details")
    print("-------------------------------------------------------------------")
    fullName = input("Full name : ")
    email = input("Email : ")


    if(re.search(regex,email)): 

        #Menu of the issues
        print("\nPlease select an issue from the following")
        print("------------------------------- MENU ------------------------------")
        print("1 : Ransomware Attack")
        print("2 : IoT Attack")
        print("3 : Cloud Attack")
        print("4 : Phishing Attack")
        print("5 : Other....")
        issueNumber = int(input("Enter issue number (1, 2, 3, 4 or 5) : "))

        #Determining the issue of the customer
        if issueNumber == 5:
            issue = input("\nEnter your issue : ")
        elif issueNumber == 1:
            issue = "Ransomware Attack"
        elif issueNumber == 2:
            issue = "IoT Attack"
        elif issueNumber == 3:
            issue = "Cloud Attack"
        elif issueNumber == 4:
            issue = "Phishing Attack"
        else:
            print("Invalid input")

        
        #Assigning each customer issue to the relevant researcher
        if (issueNumber == 1 or issueNumber == 2):
            text_file = open("researcher_1.txt", "a+")
            n = text_file. write('------------------------- CUSTOMER DETAILS ------------------------')
            n = text_file. write('\nFull name : ' + fullName + '\nEmail : ' + email + '\nIssue : ' + issue + '\n\n')
            text_file.close()

            print("\nYour customer details have been assigned to our security researcher 01")
            print("A review will be sent to your email shortly...")

        elif (issueNumber == 3 or issueNumber == 4):
            text_file = open("researcher_2.txt", "a+")
            n = text_file. write('------------------------- CUSTOMER DETAILS ------------------------')
            n = text_file. write('\nFull name : ' + fullName + '\nEmail : ' + email + '\nIssue : ' + issue + '\n\n')
            text_file.close()

            print("\nYour customer details have been assigned to our security researcher 02")
            print("A review will be sent to your email shortly...")

        elif (issueNumber == 5):
            text_file = open("researcher_3.txt", "a+")
            n = text_file. write('------------------------- CUSTOMER DETAILS ------------------------')
            n = text_file. write('\nFull name : ' + fullName + '\nEmail : ' + email + '\nIssue : ' + issue + '\n\n')
            text_file.close()

            print("\nYour customer details have been assigned to our security researcher 03")
            print("A review will be sent to your email shortly...")

        else:
            print("Invalid input")


        #Application end     
        print("\n-------------------------------------------------------------------")
        response = input("Would you like to enter another customer response? (Yes or No) : ")

        if (response == "Yes" or response == "yes"):
            print("\n\n-------------------------------------------------------------------")
            customer()
        elif (response == "No" or response == "no"):
            print("\n\n-------------------------------------------------------------------")
            print("Thank you for using our security response application")
            print("You will be directed back to the login page!")
            print("-------------------------------------------------------------------")
        else:
            print("\nInvalid input")
            print("-------------------------------------------------------------------")  


    else:   
        print("You have entered an incorrect email! \nYou will be directed back to the customer login!")   
        customer()
    



    

