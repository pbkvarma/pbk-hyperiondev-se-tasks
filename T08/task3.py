'''
Task 8 Looping using "For Statement"
Code Author: Bharat Penumathsa
Id: BP23010007956

'''
#Goal: To develop a code that prints stars('*') in ascending (increasing) order, with a number given as
#input by the user, representing No of times the "For Loop" should run printing stars('*')
given_number = int(input("\nPlease enter a number (integer > zero) representing No of times [For Loop] should run printing '*': "))

#if statement checks for invalid input i..e negative integer or a zero and prints error message if it is true. 
if given_number <= 0:
    print("\nError: Invalid! input. Please type valid input.\n")

else:
    stars = "*"
    print("\n")
    #user input (given_number) is taken as an end argument for range() so that '*' is printed that many times.
    for num in range(0, given_number):     #'num' in for loop is just any temporary variable 
        print(f"{stars}")
        stars += "*"
    print("\n")
