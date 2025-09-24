"""
The zip function combines multiple lists into a single list.
"""

roll = [101, 102, 103]
name = ["Manik", "Rahul", "Surya"]
gpa = [7.2, 9.5, 8.9]

print(list(zip(roll, name, gpa, "ABA")))


"""
[(101, 'Manik', 7.2, 'A'), (102, 'Rahul', 9.5, 'B'), (103, 'Surya', 8.9, 'A')]

"""
