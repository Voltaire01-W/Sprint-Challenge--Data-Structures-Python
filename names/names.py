import time
from names_bst import BSTNode
start_time = time.time()

f = open('C:/Users/Voltaire22/Desktop/Voltaire22/Sprint-Challenge--Data-Structures-Python/names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('C:/Users/Voltaire22/Desktop/Voltaire22/Sprint-Challenge--Data-Structures-Python/names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure
names_bst = BSTNode("")

# Replace the nested for loops below with your improvements
for name in names_1:
    names_bst.insert(name)

for name in names_2:
    if names_bst.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")