def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

num = int(input("Please enter any last number for the Fibonacci Series: "))
print(f"Fibonacci series up to {num}: ", end="")
for i in range(num):
    print(fibo(i), end=" ")


"""
Please enter any last number for the Fibonacci Series: 9
Fibonacci series up to 9: 0 1 1 2 3 5 8 13 21 

"""
