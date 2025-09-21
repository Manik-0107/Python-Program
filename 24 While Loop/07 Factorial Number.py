# Find the factorial of a number using a while loop.

num = int(input("Please enter any number: "))

i = 1
fact = 1

while i <= num:
    fact = fact * i
    i += 1

print(f"{num} factorial is: {fact}")


"""
Please enter any number: 7
7 factorial is: 5040

"""
