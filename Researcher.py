def researcher():
    print("\nWelcome to Security research team!")

    #Research Ids (1010, 1020, 1030)
    researcherId = input("Please login using the researcher id : ")

    if(researcherId == "1010"):
        print("\nWelcome Back Shamri Salman Mohamed!")
        print("Following are the pending issues to be reviewed...\n\n")

        #Reading details in from file
        with open('researcher_1.txt') as text_file:
            contents = text_file.read()
            print(contents)

        print("\n-------------------------------------------------------------------") 
        loginAsReseacher()

    elif(researcherId == "1020"):
        print("\nWelcome Back Dewshi Kulathunga!")
        print("Following are the pending issues to be reviewed...\n\n")

        #Reading details in from file
        with open('researcher_2.txt') as text_file:
            contents = text_file.read()
            print(contents)

        print("\n-------------------------------------------------------------------") 
        loginAsReseacher()

    elif(researcherId == "1030"):
        print("\nWelcome Back Nisini Weerathunga!")
        print("Following are the pending issues to be reviewed...\n\n")

        #Reading details in from file
        with open('researcher_3.txt') as text_file:
            contents = text_file.read()
            print(contents)

        print("\n-------------------------------------------------------------------")
        loginAsReseacher()

    else:
        print("\nYou are not a registered researcher")
        loginAsReseacher()
        

#Function to login as a researcher again or exit
def loginAsReseacher():
    response = input("Do you want to login in again as a researcher? (Yes or No) : ")

    if (response == "Yes" or response == "yes"):
        print("\n\n-------------------------------------------------------------------")            
        researcher()

    elif (response == "No" or response == "no"):

        print("\n\n-------------------------------------------------------------------")
        print("Thank you! \nYou will be directed back to the login page!")         
        print("-------------------------------------------------------------------")
        
    else:
        print("\nInvalid input")
        print("-------------------------------------------------------------------")

