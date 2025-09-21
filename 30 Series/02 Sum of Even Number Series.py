# Series: Sum of all numbers in the series (2 + 4 + 6 +....... + n)

num = int(input("Please enter the series last number: "))
sum = 0
for i in range(2, num+1, 2):
    if i < num:
        print(i, " + ", end=" ")
    if i == num:
        print(num, " = ", end=" " )
    
    sum += i

print(sum)




"""
Please enter the series last number: 11
2  +  4  +  6  +  8  +  10  +  30

"""
