# xxargs = xx arguments

def student(*details):
    print(details)
    print(details[0])

student(101, "Manik")
student(102, "Rahul", 25)



"""

(101, 'Manik')
101
(101, 'Rahul', 25)
101

"""
