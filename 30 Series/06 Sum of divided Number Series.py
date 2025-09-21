# 1 + 1/2 + 1/3 + ....... + 1/n = sum

num = int(input("Please enter any last of series: "))
sum = 0
for i in range(1, num+1, 1):
    if i == 1:
        print("1 + ", end="")
    if 1 < i <num:
        print("1/",i," + ", end="")
    if i == num:
        print("1/", i, end="")
    sum += (1/i)
print(" = ", sum)





"""
Please enter any last of the series: 7
1 + 1/ 2  + 1/ 3  + 1/ 4  + 1/ 5  + 1/ 6  + 1/ 7 =  2.5928571428571425


"""
