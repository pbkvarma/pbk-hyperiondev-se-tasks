"""
Task 2.1
author: Bharat Penumathsa
Id: BP23010007956
"""
#Goal: how to use strip() method to remove starting and trailing characters 
#string manupulation using string() method
hero = "$$$Superman$$$"
#Can also use strip method independently like in syntax line 10. Both will give the same result
#hero.strip("$")
print("\nhero.strip(""$""): {}\n".format(hero.strip("$")))