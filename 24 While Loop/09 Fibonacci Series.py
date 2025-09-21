# Generate the Fibonacci sequence up to N terms using a while loop.

n = int(input("Please enter any number: "))
first = 0
second = 1
print(first, second, end=" ")

i = 3

while i <= n:
    fibo = first + second
    first = second
    second = fibo
    print(fibo, end=" ")
    i += 1 



"""
Please enter any number: 7
0 1 1 2 3 5 8 

"""
