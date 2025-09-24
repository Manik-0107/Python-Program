def fact(n):
    if n ==1 :
        return 1
    else:
        return n*fact(n-1)

num = int(input("\nPlease enter any number: "))

print(f"{num}! = ", fact(num))




"""
Please enter any number: 5
5! =  120

"""
