"""
The map() / filter() function can be expressed using list comprehensions to make the program even simpler.
"""

# List comprehensions for map() function using list
num = [1, 2, 3, 4, 5]
result = [x*x for x in num]
print("Map: ", result)


# List comprehensions for filter() function using list
number = [1, 2, 3, 4, 5]
result = [x for x in number if x%2==0]
print("Filter: ", result)



"""
Map:  [1, 4, 9, 16, 25]
Filter:  [2, 4]

"""
