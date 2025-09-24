"""
--> map() can only receive 2 parameters.
    1. function - func
    2. iterl - Iterle
--> So, we can pass only these 2 parameters in the map function.
--> map(func, iterl)
"""




# Using map() function

def square(x):
    return x*x

num = [1, 2, 3, 4, 5]

result = list(map(square, num))
print(result)



"""
[1, 4, 9, 16, 25]
"""
