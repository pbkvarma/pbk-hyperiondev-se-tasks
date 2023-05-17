'''
Task 15 User input data stored as written output in a text file 
Code Author: Bharat Penumathsa
Id: BP23010007956

'''
#Goal: Code to create and write students data into a text file so 
#that students are allowed to register for exams

try: 
    while True: 

        user_input = int(input("\nPlease enter the number of students registered to take the exam: "))
  
        if user_input <= 0:

            print('\n Number of students should be greater then zero.')
            continue
        
        else:

            #A new text file to read and write is created if it doesn't exist
            with open('reg_form.txt', 'w+') as new_file:

                for number in range(user_input):
                    print("\nPlease type your ID")
                    id_no = (input("ID number: "))
                    signature = "............................."
            
                    #developing a format [number + ID No + blank for signature] to be written to the file
                    output_format = f'{number + 1}. ' + 'ID number: ' + id_no + '  ' + signature
                    #writing to the text file
                    new_file.write(output_format + '\n' + '\n')
            new_file.close()
            print("\nAll registered students ID's are written to the file\n")
            break

except:

    print('\nInvalid Input\n') 
    
    

    
