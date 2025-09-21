# Series: Sum of natural number (1 + 2 + 3 + ......... +n)

n = int(input("Please enter any last number of the natural number series: "))
sum = 0

for i in range(1, n+1, 1):
    if i<n:
        print(i," + ", end=" ")
    if i==n:
        print(n, " = ", end=" ")
    sum += i

print(sum)





"""
Please enter any last number of the natural number series: 5
1  +  2  +  3  +  4  +  5  =  15

"""
