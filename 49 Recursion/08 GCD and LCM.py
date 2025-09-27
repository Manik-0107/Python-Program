def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(y, x%y)

def LCM(x, y):
    return (x*y) // GCD(x, y)

n1 = int(input("Please enter any first number: "))
n2 = int(input("Please enter any second number: "))

print(f"GCD is: {GCD(n1, n2)}")
print(f"LCM is: {LCM(n1, n2)}")


"""
Please enter any first number: 12
Please enter any second number: 25
GCD is: 1
LCM is: 300

"""
