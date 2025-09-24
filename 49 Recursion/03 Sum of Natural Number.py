# Sum of natural numbers

def sumNaturalNo(n):
    if n == 1:
        return 1
    else:
        return n + sumNaturalNo(n-1)

num = int(input("Please enter the last number: "))
for i in range(1, num+1, 1):
    if i < num:
        print(i,"+", end=" ")
    if i==num:
        print(i," = ", end=" ")

print(sumNaturalNo(num))



"""
Please enter the last number: 5
1 + 2 + 3 + 4 + 5  =  15

"""
