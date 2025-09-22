num1 = {1, 2, 3, 4, 5}
num2 = set([4, 5, 6, 7])

print(num1)         # {1, 2, 3, 4, 5}
print(num2)         # {4, 5, 6, 7}

num2.add(8)
print(num2)         # {4, 5, 6, 7, 8}

num2.remove(8)
print(num2)         # {4, 5, 6, 7}

print(8 in num2)    # False
print(7 in num2)    # True

print(7 not in num2)        # False
print(9 not in num2)        # True

# Using set operation function

# Union function
print(num1 | num2)      # {1, 2, 3, 4, 5, 6, 7}

# Intersection function
print(num1 & num2)      # {4, 5}

# Difference Function
print(num1 - num2)      # {1, 2, 3}



""""
{1, 2, 3, 4, 5}
{4, 5, 6, 7}
{4, 5, 6, 7, 8}
{4, 5, 6, 7}
False
True
False
True
{1, 2, 3, 4, 5, 6, 7}
{4, 5}
{1, 2, 3}

"""
