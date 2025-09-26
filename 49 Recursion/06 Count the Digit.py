def cunt(num):
    if num == 0:
        return 0
    else:
        return 1+cunt(num//10)

n = int(input("Please enter any number: "))
print(f"Count of {n} is: {cunt(n)}")



"""
Please enter any number: 258
Count of 258 is: 3

"""
