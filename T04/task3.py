'''
Task 4.1
Code Author: Bharat Penumathsa
Id: BP23010007956

'''
# Goal: Program to determine the award a person competing in a triathlon will receive using if, elif, else statements
# The program reads in the times (in minutes) for all three events of a triathlon, namely swimming, cycling, and running, 
# and then calculate and display the total time taken to complete the triathlon
swim_time = int(input("\nPlease enter time taken by the Athlete in the swimming event in minutes: "))
cycle_time = int(input("Please enter time taken by the Athlete in the cycling event in minutes: "))
run_time = int(input("Please enter time taken by the Athlete in the running event in minutes: "))
total_time = swim_time + cycle_time + run_time

#Defining a List with list of awards as elements
awards = ['Provincial Colours', 'Provincial Half Colours', 'Provincial Scroll', 'No award']

#if statement checks if triathlon is completed within 100 minutes by the athlete, if so prints as winner with provincial colours
if total_time <= 100:
    print("\nCongratulations! You are a winner and you are awarded: ", awards[0],'\n')

#elif statement checks if triathlon is completed between 100 and 105 (included) minutes by the athlete, if so prints as winner with provincial half colours
elif total_time <= (100 + 5):
    print("\nCongratulations! You are a winner and you are awarded: ", awards[1],'\n')

#elif statement checks if triathlon is completed between 105 and 110 (included) minutes by the athlete, if so prints as winner with provincial scroll colours
elif total_time <= (100 + 10):
    print("\nCongratulations! You are a winner and you are awarded: ", awards[2],'\n')

#else statement checks if triathlon is completed beyond 110 minutes by the athlete, if so prints as not a winner of any award
else:
    print("\nThank you for partcipation, Sorry! You have: ", awards[3],'\n')