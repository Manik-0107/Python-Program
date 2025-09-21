# Reverse Number

num = int(input("Please enter any number: "))

sum = 0
temp = num
while temp != 0:
    rem = temp % 10
    sum = (sum*10) + rem
    temp = temp // 10

print(num, "Reverse number is: ", sum)



"""
Please enter any number: 125
125 Reverse number is:  521

"""
