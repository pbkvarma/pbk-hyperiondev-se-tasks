'''
Task 7 Looping using while statement
Code Author: Bharat Penumathsa
Id: BP23010007956

'''
#Goal: To develop a code that calculates the average of the numbers entered 
#by the user, untill he/she stops the program by typing '-1'. The code takes 
#all integers as input both negative and positive and gives the option to the 
# user if he/she wants to include or exclude '-1' as a number or not.

#Defining an empty list, to store all typed integers
nums=[]
while True:
    user_input = input("\nPlease input numbers (integers) or type '-1' to stop and wish to find the average: ")
    try:
        
        #If statement checks and appends the input to the list untill input is not '-1'
        if user_input != '-1':
            userinput_int = int(user_input)
            nums.append(userinput_int)
        
        else:
            #Code to give the user the option to include or exclude '-1' as a number to calculate average
            include = input("\nWould you like to include '-1' as a number to calculate average?\nType 'y' for YES or 'n' for NO (y/n): ")
            if include == 'y':
                userinput_int = int(user_input)
                nums.append(userinput_int)
            else:
                print("\nThank you! for using the AVERAGE calculator.\n")
                break
        
        #To find average of all the numbers typed by the user
        average = sum(nums) / len(nums)
        print(f"\nList of numbers typed: {nums}")
        print(f"Number of integers typed: {len(nums)}")
        print(f"Average of numbers: {average}")

    # To flag error if no or invalid input is typed
    except:
        print('\nSorry! Not a number (integer), Please enter a number.')
