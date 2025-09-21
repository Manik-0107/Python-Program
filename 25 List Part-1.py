subjects = ["C", "C++", "Python"]

print("All: ",subjects)
print("Index value: ", subjects[1])
print("Start & end: ", subjects[1: ])
print("Reverse: ", subjects[-1])

# Check the item is present / not-present in the list
print("Python is Present: ", "Python" in subjects)
print("Python is not present: ", "Python" not in subjects)

# Add items in the list
print(subjects + ["Java", 7])

# Items are print many times
print(subjects * 3)

print()




"""
All:  ['C', 'C++', 'Python']
Index value:  C++
Start & end:  ['C++', 'Python']
Reverse:  Python
Python is Present:  True
Python is not present:  False
['C', 'C++', 'Python', 'Java', 7]
['C', 'C++', 'Python', 'C', 'C++', 'Python', 'C', 'C++', 'Python']

"""
