# Slicing and Indexing with Strings
#   - You can pass a specific character count
#
# Example: You can slice strings into numbers
#
# "H e l l o   W o r l d"
# "0 1 2 3 4 5 6 7 8 9 10"

mystring = "Hello World"
print("Your string is: ", mystring)

print("The first letter is", mystring[0])
print("The second letter is", mystring[1])
print("The eighth letter is", mystring[8])

# You can also use reverse indexing
#
# Example: This will start from the last as -1
#
# "  H   e  l   l   o      W  o  r  l  d"
# "-11 -10 -9  -8  -7  -6 -5 -4 -3 -2 -1"

mystring = "Hello World"
print("\nYour string is: ", mystring)

print("The last letter is", mystring[-1])
print("The second to the last letter is", mystring[-2])