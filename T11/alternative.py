'''
Task 11 String handling
Code Author: Bharat Penumathsa
Id: BP23010007956

'''
#Goal: Code to convert a user input string's alternative character to 
#lowercase[odd index] or uppercase[even index]. Further convert the same 
#string's alternative word to lowercase[even index] or uppercase[odd index]

input_str = input("\nPlease type a string example - 'Hello World': ")

#printing original string
print("\nThe string typed is : " + str(input_str))

# Defining empty string
result_string = ""

for index in range(len(input_str)):

    #for string character representing even index
    if index % 2 == 0:     #can also use 'not index % 2:'instead
        result_string = result_string + input_str[index].upper()
    
    #for string character representing odd index
    else:
	    result_string = result_string + input_str[index].lower()

#printing case altered string
print("\nThe altered alternative case string character is : " + str(result_string) + '\n')

#split() method to convert string to a list of string elements
words = input_str.split()

result_list = []

for word in range(len(words)):

    #for string word representing even index
    if not word % 2:
        alter_string = words[word].lower()
        result_list.append(alter_string)

    #for string word representing odd index
    else:
        alter_string = words[word].upper()
        result_list.append(alter_string)

#printing the case altered string
print("The altered alternative case string word is : " + ' '.join(result_list) + '\n')
