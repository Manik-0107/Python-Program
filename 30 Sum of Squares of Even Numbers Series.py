# 2^2 + 4^2 + 6^2 + ..... + n^2

num = int(input("Please enter the last number of the even number series: "))
sum = 0
for i in range(2, num+1, 2):
    if i < num:
        print(i,"^2 + ", end="")
    if i == num:
        print(i,"^2", end="")
    sum += (i**2)
print(" = ", sum)



"""
Please enter the last number of the even number series: 11
2 ^2 + 4 ^2 + 6 ^2 + 8 ^2 + 10 ^2 +  =  220

"""
