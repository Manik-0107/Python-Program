# Check whether a number is prime using a while loop.

num = int(input("Please enter any number: "))

i = 2
flag = 0

while i < num:
    if num % i == 0:
        flag = 1
        break
    i += 1

if flag == 1:
    print(num, " is not a prime number")

else:
    print(num, " is a prime number")
    
print("\nThe Program is successfully executed")





"""
Please enter any number: 7
7  is a prime number
The program is successfully executed

Please enter any number: 22
22  is not a prime number
The program is successfully executed

"""
