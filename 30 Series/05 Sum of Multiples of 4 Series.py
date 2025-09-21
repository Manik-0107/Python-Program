# 4 + 8 + 12 ......+n

num = int(input("Please enter any last number of series: "))
sum = 0
for i in range(4, num+1, 4):
    if i < num:
        print(i," + ", end=" ")
    if i == num:
        print(i, end=" ")
    sum += i
print(" = ", sum)








"""
Please enter any last number of series: 20
4  +  8  +  12  +  16  +  20  =  60

"""
