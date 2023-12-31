# Strings are sequences of characters, using the syntax of either single quotes or double quotes:
#   - 'hello'
#   - "Hello"
#   - "I don't do that"

# Example of a string

print("Hello World")

# Another example of a string

print("This is a string")

# You need to be careful of syntax errors like a broken string
# This has invalid single quotes

#print('I'm going on a run')
      
# Example:
#
#jonathan@ctrl-ansible:~/python_learning$ /bin/python3 /home/jonathan/python_learning/python-bootcamp-stuff/section-2_object-and-data/intro_strings.py
#  File "/home/jonathan/python_learning/python-bootcamp-stuff/section-2_object-and-data/intro_strings.py", line 17
#    print('I'm going on a run')
#                             ^
#SyntaxError: unterminated string literal (detected at line 17)

# You can also use escape sequences to print out things like a new line
# \n will tell python to print a new line (just like other programming languages)

print('Hello \nWorld')

# jonathan@ctrl-ansible:~/python_learning$ /bin/python3 /home/jonathan/python_learning/python-bootcamp-stuff/section-2_object-and-data/intro_strings.py
# Hello World
# This is a string
# Hello 
# World

# The len function shows the length of strings

print(len("hello"))