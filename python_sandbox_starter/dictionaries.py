# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dictionart
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 40
}

print(person, type(person))

# Get a value out of dictionary
print(person['first_name'])
print(person.get('last_name'))

# Add key/value pair
person['phone'] = '444-444-4444'

# Get keys
print(person.keys())

# Get items
print(person.items())

# Copy the dictionary
person2 = person.copy()
person2['city'] = 'Boston'

print(person)
print(person2)

# Remove an item
del(person['age'])
print(person)
person.pop('phone')
print(person)

# Clear the dictionary
person.clear()
print(person)

# Get length

# Create list of dictionaries
people = [
    {'name': 'Mabel', 'age': 2},
    {'name': 'Mathilde', 'age': 14}
]

print(people)

# Get positional element - print Mathilde's age
print(people[1]['age'])