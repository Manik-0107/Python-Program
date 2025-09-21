# List Function

from traceback import print_tb


subjects = ["C", "C++", "Python", "Java"]

print("\nLength of list: ", len(subjects))

subjects.append("Swift")
print(subjects)

subjects.insert(2, "Go")
print(subjects)

subjects.remove("C++")
print(subjects)

subjects.pop()
print(subjects)

subjects.sort()
print(subjects)

num = [50, 20, 40, 10 , 30]
num.sort()
print(num)

num.reverse()
print(num)

num2 = num.copy()
print(num2)

position = subjects.index("Python")
print("Python index is: ", position)

num.clear()
print(num)

number = [4, 5, 2, 4, 8, 4, 9, 2, 4]
cunt = number.count(4)
print("4 is present", cunt, "times in the number list")

print()






"""
Length of list:  4
['C', 'C++', 'Python', 'Java', 'Swift']
['C', 'C++', 'Go', 'Python', 'Java', 'Swift']
['C', 'Go', 'Python', 'Java', 'Swift']
['C', 'Go', 'Python', 'Java']
['C', 'Go', 'Java', 'Python']
[10, 20, 30, 40, 50]
[50, 40, 30, 20, 10]
[50, 40, 30, 20, 10]
Python index is:  3
[]
4 is present 4 times in the number list

"""
