# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = 'Jane'
age = 37

# Concatenate : insert variable into a string
print('Hello, my name is ' + name + ' and I am ' + str(age))

# String Formatting
# Arguments by position
print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')


# String Methods

s = 'hello, world'

# Capitalize string
print(s.capitalize())

# Make upper case
print('upper: ' + s.upper())

# Make lowercase
print('lower: ' + s.lower())

# Swap cases
print('swapcase: ' + s.swapcase())

# Get length
print('len: ' + str(len(s))) # can be used on any data type

# Replace
print('replace: ' + s.replace('world', 'everyone'))

# Count
sub = 'l'
print('count: ' + str(s.count(sub)))

# Starts with
print(s.startswith('hello')) # returns boolean

# Ends with
print(s.endswith('hello'))

# Split into a list (or array)
print(s.split())

# Find position of first instance 
sub = 'l'
print(s.find(sub))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())



