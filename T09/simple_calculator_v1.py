'''
Task 09 Calculator application to calculate a equation with two numbers 
and a operand as user inputs
Code Author: Bharat Penumathsa
Id: BP23010007956

'''
# Goal: Application code with user option to read and print equations from existing text file or 
# calculate a equation given two numbers and a operand and write it to the same text file. 
# One choice of operand is to exit application. Error handling is done through try statement.

try:

    user_choice = input("\nWould you like to see equations from existing file? 'y' for yes/'n' for no: ")

    if user_choice.lower() == 'y':

        # function to read and print existing file equations.txt, if it does not exist or typed
        # wrongly flags error and gives the user to retry
        def eq_file_print():
            file_name = input("\nType existing file name as --> equations.txt: ")
            with open(file_name, 'r') as eq_file:
                print('\n')
                print(eq_file.read())


        eq_file_print()

    else:

        first_number = float(input("\nPlease enter first number: "))
        second_number = float(input("\nPlease enter second number: "))
        calculator_menu = '''User can choose a 'operand'(symbol) for the calculator to calculate.
        Please choose appropriate symbol from the following options:

                        Addition       - type '+'
                        Subtraction    - type '-'
                        Multiply       - type '*'
                        Division       - type '/'
                        Modulus        - type '%'
                        Exit app       - type 'e'.'''
        print(calculator_menu)
        operand = input("\nPlease enter the operand you want to use: ")

        # checks in the case of '/' and '%' whether 2nd number typed by the user is > 0, if not flags error
        if (operand == '/' and second_number == 0) or (operand == '%' and second_number == 0):
            print("\nZeroDivisionError: Second number should be > 0")
            second_number = float(input("\nPlease enter second number > 0: "))
            pass


        def calculator(first_number, second_number, operand):

            # A new text file to read and write is created if it doesn't exist
            with open('equations.txt', 'a') as new_file:

                # checks if user input numbers are float, if not prints error message
                if first_number == float(first_number) and second_number == float(second_number):
                    if operand == "+":
                        add = (first_number) + (second_number)
                        result = f"{first_number} + {second_number} = {add}"
                        new_file.write(result + '\n')

                    elif operand == "-":
                        subtract = (first_number) - (second_number)
                        result = f"{first_number} - {second_number} = {subtract}"
                        new_file.write(result + '\n')

                    elif operand == "*":
                        multiply = (first_number) * (second_number)
                        result = f"{first_number} * {second_number} = {multiply}"
                        new_file.write(result + '\n')

                    elif operand == "/":
                        divide = (first_number) / (second_number)
                        result = f"{first_number} / {second_number} = {divide}"
                        new_file.write(result + '\n')

                    elif operand == "%":
                        modulus = (first_number) % (second_number)
                        result = f"{first_number} % {second_number} = {modulus}"
                        new_file.write(result + '\n')

                    elif operand == "e":
                        # Clean exit of app without any errors / problems
                        exit(0)

                    else:
                        # checks if right operand is typed by the user, if not flags error and asks to re-enter
                        print(calculator_menu)
                        print("\nInvalid! input. No valid operand is given by the user, refer to the menu")
                        operand = input("\nPlease enter valid operand from the menu: ")
                        calculator(first_number, second_number, operand)

                else:
                    print("Try again")
                    first_number = float(input("\nPlease enter first number: "))
                    second_number = float(input("\nPlease enter second number: "))
                    calculator(first_number, second_number, operand)


        # function call with arguments
        calculator(first_number, second_number, operand)

except FileNotFoundError:
    print("\nSorry! The 'equations' text file does not exist")
    print("\nTry again, this time type file name correctly.")
    # Re-run the file read function if error is flaged. Refer to line 18 to 19
    eq_file_print()

except ValueError:
    print("\nSorry! Invalid string input. Should be an integer or a float number\n")

finally:
    print("\nThanks! for using the 'CALCULATOR' app\n")
