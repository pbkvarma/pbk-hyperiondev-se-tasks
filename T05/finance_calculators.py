'''
Task 5 Capstone Project
Code Author: Bharat Penumathsa
Id: BP23010007956

'''
#Goal to develop a code so that the user can access through choice and calculate two different 
# financial calculators:an investment calculator and a home loan repayment calculator

import math #Python library to calculate math functions
#Defining a menu for the user to select the product he/she wants to invest in
#The user can type either '1' or 'investment' for investment or either '2' or 'bond' for bond
menu_op = ['1', 'investment', '2', 'bond']
print("\n                   Product Menu                          ")
print("---------------------------------------------------------")
print("Investment: Type '1' or 'investment'")
print("Bond:       Type '2' or 'bond'")
print("---------------------------------------------------------\n")
menu = input(("Please choose the product from above menu by typing either '1'/'investment' for investment or '2'/'bond' for bond: "))

if menu == menu_op[0] or menu.lower() == menu_op[1]:
    #input required from the user to calculate investment return based on simple or compound interest
    principle_amount = float(input("\nPlease enter the amount you want to deposit: "))
    interest_rate = float(input("Please enter the interest rate you are expecting: "))/100 #divided by 100 to convert % to float
    #print(interest_rate) #just to check if interest rate is converted to float
    years = float(input("Please enter the number of years you plan to invest: "))

    #Defining an interest list which has two elements 'simple' and 'compound'
    interest_op = ['simple', 'compound']
    print("\nYou can choose Simple Interest or Compound Interest")
    interest = input("Please enter whether you want to use [Simple Interest] by typing 'simple' or [Compund Interest] by typing 'compound': ")
    #if statement to calculate simple interest
    if interest.lower() == interest_op[0]:
        total_amount_si = principle_amount * (1 + interest_rate * years)
        print(f"\nTotal amount you will recieve with simple interest: {round(total_amount_si,2)}\n")
    #elif statement to calculate compound interest
    elif interest.lower() == interest_op[1]:
        total_amount_ci = principle_amount * math.pow((1 + interest_rate), years)
        print(f"\nTotal amount you will recieve with compound interest: {round(total_amount_ci,2)}\n")
    #error management if typed invalid input
    else:
        print("\nSorry! You haven't typed valid input, please choose right choice\n")

elif menu == menu_op[2] or menu.lower() == menu_op[3]:
    #input required from the user to calculate bond repayment
    house_value = float(input("\nThe present value of your house: "))
    bond_interest_rate = float(input("The interest rate you are willing to pay: "))/100 #divided by 100 to convert % to float
    montly_interest_rate = bond_interest_rate/12   #divided by 12 to distribute monthly
    months = int(input("The number of months you plan to take to repay the bond: "))

    #formula to calculate bond repayment
    repayment_per_month = (montly_interest_rate * house_value)/(1 - (1 + montly_interest_rate) ** (-months))

    #prints total amount to repay each month rounded to two digits
    print(f"\nTotal amount you have to repay each month: {round(repayment_per_month,2)}\n")

#error management if user typed invalid input
else:
    print("\nSorry! You haven't typed valid input, please choose right choice\n")



