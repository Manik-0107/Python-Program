# GCD = Greatest Common Divisor
# LCM = Least Common Multiple

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def lcm(a, b):
    return (a*b)/gcd(a, b)

num1 = int(input("Please enter any first number: "))
num2 = int(input("Please enter any second number: "))

print("GCD: ", gcd(num1, num2))
print("LCM: ", lcm(num1, num2))


"""
Please enter any first number: 12
Please enter any second number: 25
GCD:  1
LCM:  300.0

"""
