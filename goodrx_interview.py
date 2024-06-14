# print(message.status)
# print(data["list"][0]["weather"])  # Weather ID and description
# Test logic
# list = [4, 5, 3, 6]
# for num in list:
#     if num < 5:
#         less = True
#
# if less:
#     print("value is less than 5")
# else:
#     print("Not less than 5")

def indexSort(arr, indices):

    # Reverse the indices list because Python's sort() function sorts by the last key provided first
    # when sorting by multiple keys. We want the first element in indices to be the primary key.
    indices.reverse()

    # Apply sorting with a compound key
    arr.sort(key=lambda x: tuple(
        (x[index], -x[index] if descending else x[index])
        for index, descending in indices
    ))
    return arr


# Example usage
a = [[1, 2, 1], [3, 3, 1], [4, 2, 3], [6, 4, 3]]
ind = [[1, 0], [2, 1]]  # Column 1 ascending, Column 2 descending

indexSort(arr=a, indices=ind)
print(a)


