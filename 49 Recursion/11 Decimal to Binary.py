# Using str() function
def decimal_to_binary(num):
    if num == 0:
        return ""
    else:
        return decimal_to_binary(num//2) + str(num%2)

num = int(input("Please enter any decimal number: "))
print("Binary number is: ", decimal_to_binary(num))

# Decimal to Binary without using str()
"""
def decimal_to_binary(num):
    if num == 0:
        return 0
    else:
        return decimal_to_binary(num//2) + num%2
"""

# Output
"""
Please enter any decimal number: 7
Binary number is:  111
"""
