# Count the number of digits in a number using a while loop.

num = int(input("Please enter any number: "))

sum = 0
temp = num
while temp != 0:
    rem = temp % 10
    sum = sum + 1
    temp = temp // 10

print(num, "number of digits is: ", sum)



"""
Please enter any number: 12587
12587 number of digits is:  5

"""
