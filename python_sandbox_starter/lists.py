# A List is a collection which is ordered and changeable. Allows duplicate members.
# Similar to arrays

# Create a lists
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# # Use a constructor
# numbers2 =list((1, 2, 3, 4, 5))

# print(numbers, numbers2)

print(fruits[1])
print(len(fruits))

# Add to a list

fruits.append('Mangoes')

# Add multiples to a list
fruits.extend(['Guava', 'Pineapple'])

# Remove from list
fruits.remove('Oranges')

# Insert into particular position of list
fruits.insert(2, 'Oranges')

# Remove with pop to remove something from a particular position
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort Alphabetically
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

# Change a value
fruits[0] = 'Dragonfruit'

print(fruits)
# print(type(fruits))