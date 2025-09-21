#Check whether a number is an Armstrong number using a while loop.

num = int(input("Please enter any integer number: "))

sum = 0
temp = num

while temp != 0:
    rem = temp % 10
    sum = sum + (rem ** 3)
    temp //= 10

if sum == num:
    print("\n",num, "is an Armstrong number.")
    print("Becase: ",num," = ", sum)
else:
    print("\n",num, "is not an Armstrong number.")
    print("Becase: ",num," != ", sum)




"""
Please enter any integer number: 1583

1583 is not an Armstrong number.
Because:  1583  !=  665



Please enter any integer number: 153

153 is an Armstrong number.
Because:  153  =  153

"""
