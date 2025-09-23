# Returning value from function

def large(a, b):
    if a > b:
        return a
    else:
        return b

# 1st way
# print("Max Value: ",large(33, 11))

# 2nd way
# max = large(50, 20)
# print("Max Value: ",max)

# 3rd way
maximum = large
print("Max Value: ",maximum(40, 70))



"""

Max Value:  70

"""
