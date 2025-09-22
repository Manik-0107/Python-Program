student = {
    "101" : "Manik Mondal",         # 101 : "Manik Mondal"
    "102" : "Rahul Mondal",         # 102 : "Rahul Mondal"
    "103" : "Surya Mondal"          # 103 : "Surya Mondal" 
}                                   # You can use int, string

print(student["101"])       # Manik Mondal
# print(student["107"])     # KeyError '107'

print(student.get("103"))   # Surya Mondal
print(student.get("106"))   # None

print(student.get("107", "Not a valid Key"))        # Not a valid key
print(student.get("101", "Not a valid key"))        # Manik Mondal




"""

Manik Mondal
Surya Mondal
None
Not a valid Key
Manik Mondal

"""
