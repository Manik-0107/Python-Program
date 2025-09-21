# Sum of natural numbers 1 to n
# 1 + 2 + 3 + .................... + n
# n = 10
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 =  55

n = int(input("Please enter any ending number: "))

sum = 0
i = 1
while i <= n:
    if i < n:
        print(f"{i} + ", end="")
    if i == n:
        print(f"{i} = ", end="")
    sum += i
    i += 1

print(f" {sum}")
print(f"Sum of {n} numbers is: {sum}")
print("\nThe Program is successfully executed")



"""
Please enter any ending number: 10
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 =  55
Sum of 10 numbers is: 55

The program is successfully executed

"""
