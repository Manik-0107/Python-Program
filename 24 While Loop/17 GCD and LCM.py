# Find the Greatest Common Divisor (GCD) of two numbers using while loop.
# Find the Least Common Multiple (LCM) using while loop.

num1 = int(input("Enter any first number: "))
num2 = int(input("Enter any second number: "))

n1 = num1
n2 = num2

while n2 != 0:
    rem = n1 % n2
    n1 = n2
    n2 = rem 

gcd = n1
lcm = (num1 * num2)/gcd

print("GCD: ", gcd)
print("LCM: ", lcm)





"""
Enter any first number: 20
Enter any second number: 14
GCD:  2
LCM:  140.0

"""
