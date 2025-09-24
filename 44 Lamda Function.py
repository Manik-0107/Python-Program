""" Defination
--> A function without a name that is called a Lambda Function.
--> A Lambda function is also called an Anonymous function, because it has no name.
--> Not as powerful as the name function
--> It can work with a single expression / single line of code

"""


# Calculate (a + b)^2 = ? using lamda function

# print((lambda a, b : a*a + 2*a*b + b*b)(2, 3))

a = (lambda a, b : a*a + 2*a*b + b*b)(2, 3)
print("(2 + 3)^2 = ", a)

print("2^3 = ", (lambda x : x*x*x)(2))


# Output
"""
(2 + 3)^2 =  25
2^3 =  8

"""
