# Find the sum of digits of a number using a while loop.

num = int(input("Please enter any number: "))

sum = 0
temp = num

while temp != 0:
    rem = temp % 10
    sum += rem
    temp //= 10

print("\n",num, "sum of digits is: ", sum)
print("Program is successfully executed\n") 




"""
Please enter any number: 1258

 1258 sum of digits is:  16
Program is successfully executed

"""
