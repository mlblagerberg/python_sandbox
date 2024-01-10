# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
people = ['Mabel', 'Mathilde', 'Alexey', 'Madeleine']

# Simple for loop
# for person in people:
#     print(f'Current Person: {person}')

# Break - stops loop once it gets to person in if statement
for person in people:
    if person == 'Alexey':
        break
    print(f'Current Person: {person}')

# Continue - basically skips the person listed in the if statement
for person in people:
    if person == 'Alexey':
        continue
    print(f'Current Person: {person}')

# Range
for i in range(len(people)):
    print(people[i])

for i in range(0,11):
    print(f'Number: {i}')



# While loops execute a set of statements as long as a condition is true.
count = 0 
while count <= 10:
    print(f'Count: {count}')
    count = count + 1 # short hand is count +=1
