# Creating an empty list called my_list
my_list = []

# Appending elements to my_list: 10, 20, 30, 40
my_list.extend([10, 20, 30, 40])

# Inserting the value 15 at the second position in the list
my_list.insert(1, 15)

# Extending my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# Removing the last element from my_list
my_list.pop()

# Sorting my_list in ascending order
my_list.sort()

# Find and print the index of the value 30 in my_list
index_30 = my_list.index(30)
print("Index of value 30 in my_list:", index_30)

# Printing the final list
print("Final list:", my_list)