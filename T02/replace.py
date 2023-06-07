"""
Task 2.2
author: Bharat Penumathsa
Id: BP23010007956
"""
#Goal: Using replace(), upper() methods and slicing to reverse a string
long_string = "The!quick!brown!fox!jumps!over!the!lazy!dog!."
string_replace = long_string.replace("!", " ").replace(" .", ".")
string_upper = string_replace.upper()
#String can be reversed using slicing start:stop:step. -1 represents from the last index
string_reverse = string_upper[::-1]
#Can also use reversed and join methods to reverse string. Reversed() reads one character at a time, so join is needed 
string_reverse_2 = "".join(reversed(string_upper))
print("\nString replaced : {}".format(string_replace))
#Another way of using format
#print(f"String replaced : {string_replace}")
print("String uppercase : {}".format(string_upper))
print("String reverse : {}\n".format(string_reverse))