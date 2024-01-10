# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value tuple needs a trailing comma
fruits2 = ('Apples',) # VS ('Apples') which would return type string
print(fruits, fruits2)

# Get value
print(fruits[1])

# Can't change value
# fruits[0] = 'Pears'

# del fruits2
# print(fruits2)

print(len(fruits))



# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Bananas'}

# Check if value is in set
print('Grapes' in fruits_set)

# Add to set
fruits_set.add('Grapes')
print(fruits_set)

# Try to add a duplicate
fruits_set.add('Apples')
print('still only one Apples instance: ')
print(fruits_set)

# Remove from set
fruits_set.remove('Apples')
print(fruits_set)

# Clear set leaves an empty set
fruits_set.clear()
print(fruits_set)

# Delete a set
# del fruits_set
# print(fruits_set)
