# If/ Else conditions are used to decide to do something based on something being true or false

x = 13
y = 1

# # Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# # Simple if
# if x > y:
#     print(f'{x} is greater than {y}')


# # If else
# if x > y:
#     print(f'{x} is greater than {y}')
# else:
#     print(f'{y} is greater than {x}')

# # There is an issue with this if else, since it doesn't consider the case when the values are equal. Let's use an ifel to consider this case
    
# if x > y:
#     print(f'{x} is greater than {y}')
# elif x == y :
#     print(f'{x} and {y} are equal') 
# else:
#     print(f'{y} is greater than {x}') 

# # Nested if statements (not advised, should use logical operators instead)
# # if x > 2:
# #     f x<= 10:
# #         print(f'{x} is greater than 2 and less than or equal to 10')

# # Logical operators (and, or, not) - Used to combine conditional statements
# # And
# if x > 2 and x <= 10:
#    print(f'{x} is greater than 2 and less than or equal to 10') 

# # Or
   
# # Not
# if not(x == y):
#     print(f'{x} is not equal to {y}')


# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object

# numbers = [1,2,3,4,5,6]

# if x in numbers:
#     print(x in numbers)

# if x not in numbers:
#     print(x not in numbers)


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

if x is y:
    print(x is y)

if x is not y:
    print(x is not y)