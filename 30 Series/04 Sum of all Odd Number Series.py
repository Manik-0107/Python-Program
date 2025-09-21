# Series: Sum of all Odd numbers in the series (1 + 3 + 5 + ......... +n)

num = int(input("Please enter any last number: "))
sum = 0
for i in range(1, num+1, 2):
    if i < num:
        print(i, " + ", end=" ")
    if i == num:
        print(num, " = ", end=" ")
    sum += i
print(sum)




"""
Please enter any last number: 7
1  +  3  +  5  +  7  =  16

"""
