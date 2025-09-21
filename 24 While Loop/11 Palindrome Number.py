# Check whether a number is a palindrome using a while loop.

num = int(input("Please enter any integer number: "))

sum = 0
temp = num
while temp != 0:
    rem = temp % 10
    sum = (sum*10) + rem
    temp //= 10

if sum == num:
    print(num, "is a Palindrome number")

else:
    print(num, "is not a Palindrome number")




"""
Please enter any integer number: 727
727 is a Palindrome number

Please enter any integer number: 725
725 is not a Palindrome number

"""
