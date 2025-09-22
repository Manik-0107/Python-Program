student = (
    "Manik Mondal",
    "Rahul Mondal",
    "Surya Mondal"
)

print()
print(student)          # ('Manik Mondal', 'Rahul Mondal', 'Surya Mondal')
print(student[0])       # Manik Mondal

# student[0] = "Jack Kelvin"
# print(student[0])           # TypeError: 'tuple' object does not support item assignment

# Inner Tuples
students = (
    ("Manik", 24, 7.21),
    "Jack Kelvin",
    "Shreya Patil"
)
print(students)     # (('Manik', 24, 7.21), 'Jack Kelvin', 'Shreya Patil')
print(students[0])  # ('Manik', 24, 7.21)

print(students[1:])

print("\nThe program is successfully executed...\n\n")





"""

('Manik Mondal', 'Rahul Mondal', 'Surya Mondal')
Manik Mondal
(('Manik', 24, 7.21), 'Jack Kelvin', 'Shreya Patil')
('Manik', 24, 7.21)
('Jack Kelvin', 'Shreya Patil')

The program is successfully executed...

"""
