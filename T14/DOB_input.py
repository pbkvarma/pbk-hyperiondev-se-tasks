'''
Task 14 External data as input from a text file 
Code Author: Bharat Penumathsa
Id: BP23010007956

'''
#Goal: Code to open and read data from a external text file and printing 
#out the data into two different coloumns  

#Empty list for names 
name_list = []
#Empty list for birthdate
dob_list = []

#file opening and reading line by line [Note: if using 'with' statement, need not use file.close]
with open('DOB.txt', 'r') as input_file:
    for line in input_file:
        #split() method splits a line of string into elements while removing '\n'
        file_list = line.split()

        name = file_list[0] + ' ' + file_list[1]
        #Name list is created with first & second name
        name_list.append(name)
        
        dob = file_list[2] + ' ' + file_list[3] + ' ' + file_list[4]
        #date of birth list is created
        dob_list.append(dob)
    
    #code syntax to print 'Name' in bold
    print("\n\033[1mName\033[0m")
    #To print 'Name' as a seperate column
    for index in range(len(name_list)):
        print(name_list[index])
    print('\n')

    #code syntax to print 'Birthdate' in bold
    print("\n\033[1mBirthdate\033[0m")
    #To print 'Birthdate' as a seperate column
    for index in range(len(dob_list)):
        print(dob_list[index])
    print('\n')
    