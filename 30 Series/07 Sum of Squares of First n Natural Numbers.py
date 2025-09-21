# Series: Sum of natural number square series: 1^2 + 2^2 + 3^2+ .... + n^2

num = int(input("Please enter any last number of series: "))
sum = 0
for i in range(1, num+1, 1):
    if i < num:
        print(i,"^2 + ", end=" ")
    if i == num:
        print(i,"^2", end=" ")
    sum += (i**2)
print(" = ",sum)





"""
Please enter any last number of the series: 7
1 ^2 +  2 ^2 +  3 ^2 +  4 ^2 +  5 ^2 +  6 ^2 +  7 ^2  =  140

"""
