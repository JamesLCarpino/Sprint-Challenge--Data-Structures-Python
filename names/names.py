import time

start_time = time.time()

f = open("names_1.txt", "r")
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open("names_2.txt", "r")
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# list()
# using bstnode
# from binary_search_tree import BSTNode

# fasttree = BSTNode(names_1[0])
# # now insert the names in names_1 into
# for name_1 in names_1:
#     fasttree.insert(name_1)
# # if the BST contains a name in name_2 add to duplicates list
# for name_2 in names_2:
#     if fasttree.contains(name_2):
#         duplicates.append(name_2)

# stupid fast gives 1 dictionary of the names that are duplicates
# duplicates.append(str(list(set(names_1).intersection(set(names_2)))))
# for name in names:
#     print(name)

name_list = str(list(set(names_1).intersection(set(names_2))))
duplicates.append(str(name_list))


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
