# xxargs = xx arguments

def student(*details):
    print(details)
    print(details[0])

student(101, "Manik")
student(102, "Rahul", 25)


def add(*details):
    sum = 0
    for num in details:
        sum += num
    print("Addition is: ", sum)
add(10, 20)



"""

(101, 'Manik')
101
(101, 'Rahul', 25)
101

Addition is: 30

"""
