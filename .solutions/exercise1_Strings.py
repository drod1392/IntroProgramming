# In this exercise we will be working with strings
# 1) We will be reading input from the console (similar to example2_ReadConsole.py)
# 2) We will concatenate our input strings
# 3) We will convert them to upper and lowercase strings
# 4) Print just the last name from the "name" variable
# 5) EXTRA - Use proper capitalization on first and last name

print("Section 1 - Read input\n")
# Prompt the user to enter first and last name seperately
# Use two input() commands to read first and last name seperately. 
# Use variable names "first" and "last" to store your strings

print('Please enter your first name:')
first = input()
print('Please enter your last name:')
last = input()

print("\nSection 2 - Concatenate")
# Concatenate first and last name together in variable "name"
# Print out the result

name = first + ' ' + last
print(name)

print("\nSection 3 - Upper and Lower")
# Print "name" in all uppercase
# Print "name" in all lowercase

print(name.upper())
print(name.lower())

print("\nSection 4 - Only Last Name")
# Print just the last name from "name"
start = len(first) + 1
end = len(name)
print(name[start:end])
# print(name[start:])

print("\nSection 5 - Capitalization")
# Extra - use proper capitalization on first and last name
print(first.capitalize() + ' ' + last.capitalize())