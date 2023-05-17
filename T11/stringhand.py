# Python3 code to demonstrate working of
# Alternate cases in String

# initializing string
# Python3 code to demonstrate working of
# Alternate cases in String
# Using upper() + lower() + loop

# initializing string
test_str = "geeksforgeeks bharat"

# printing original string
print("The original string is : " + str(test_str))

# Using upper() + lower() + loop
# Alternate cases in String
res = ""
for idx in range(len(test_str)):
	if idx % 2 == 0:
    #if not idx % 2:
		res = res + test_str[idx].upper()
	else:
		res = res + test_str[idx].lower()

# printing result
print("The alternate case string is : " + str(res))
