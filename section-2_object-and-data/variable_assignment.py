# You can assign variables and then call them later
# Python uses Dynamic Typing, so variables can be assigned different values and still work

# Simple Variable:

a = 5
print("This is the value of a is: ", a)

# Example of Dynamic Typing
# - The variable can be re-assigned a new value

a = 10
print("The NEW value of a is: ", a)

# If you do not know what type the variable is, you can use the type operator

print("The variable a is: ", type(a))

a = 30.123
print("The variable a is: ", type(a))

# Python variables can be much more readable.
# Example: 

my_income = 100
tax_rate = 0.1

my_taxes = my_income * tax_rate
print(my_taxes)