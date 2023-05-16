'''
Task 3.1
Code Author: Bharat Penumathsa
Id: BP23010007956

'''
#Goal: Program to validate whether the user has entered his full name, 
# if they haven’t or if they exceeded 25 characters, prints an appropriate error message.
# This code takes surname and forename as inputs from the user and combines it to print full name, if format conditions are met.
surname = input("\nPlease enter your surname or last name: ") #by default type is string for input, works even without str
forename = input("Please enter your forename or first name: ")

#For checking input
#print(len(surname)) #print(len(forename))
#The if statement checks, if surname or forename has numbers as input given by the user, if so prints error message.
if surname.isdigit() + forename.isdigit() :
    print ("Please do not enter any numbers, only strings are allowed as input.")

#The elif statement checks, if surname or forename has no input given by the user, if so prints error message.
elif len(surname) == 0 or len(forename) == 0: 
    #len(surname or forename) is not giving right output why?
    print("\nError message: You haven't entered anything. Please enter your full name.\n") 

#elif statement checks if combination of surname or forename is less then 4 characters, if so prints error message
elif len(surname + forename) < 4:
#elif len(surname or forename) < 4 or len(surname + forename) < 4: #checking if surname or forename or combination of both is less then 4 characters
    print("\nError message: You have entered less than 4 characters. Please make sure that you have entered your name and surname.\n") 

#elif statement checks if either surname or forename or a combination of both exceeds 25 characters, if so prints error message
elif len(surname) > 25 or len(forename) > 25 or len(surname + forename) > 25:
    print("\nError message: You have entered more than 25 characters. Please make sure that Have only entered your full name.\n") 

#else statement prints the full name, if it meets all the requirements of the format 
else:
    print("\nThank You! For Entering Your Name.")
    print(f"Your full name is: {surname.capitalize()} {forename.capitalize()}\n") #Caitalize's first letter of the string during print




