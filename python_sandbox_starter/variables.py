# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

"""
Docstrings under PEP 8 use the double quotes
See PEP 8 style guide for reference:
https://www.python.org/dev/peps/pep-0008/#documentation-strings
"""
 
#  x = 1 # by default this is casted as int
# y = 2.5 # by default casted as a float
# name = 'Your Mom' # casted as a string
# is_cool = False # casted as boolean

# Use Command + / to comment out multiple lines

# Multiple assignment 
x, y, name, is_cool = (1, 2.5, 'Your Mom', False)

print(x, y, name, is_cool)

# Basic math
a = x + y

print(x, y, name, is_cool, a)
print(type(a))

# Casting
x = str(x)
y = int(y)
z = float(y)

print(x, y, z)
