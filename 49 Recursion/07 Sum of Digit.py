def sum_digit(num):
    if num == 0:
        return 0
    else:
        return sum_digit(num//10) + (num%10)
num = int(input("Please enter any number: "))
print(f"Sum of {num} is: {sum_digit(num)}")



"""

Please enter any number: 345
Sum of 345 is: 12

"""
