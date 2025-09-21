# Findout largest number between 3 numbers

n1 = int(input("Please enter any 1st number: "))
n2 = int(input("Please enter any 2nd number: "))
n3 = int(input("Please enter any 3rd number: "))

if n1 > n2 and n1 > n3:
    print(f"Largest number is: {n1}")

elif n2 > n1 and n2 > n3:
    print(f"Largest number is: {n2}")

else:
    print(f"Largest number is: {n3}")



"""
Please enter any 1st number: 20
Please enter any 2nd number: 30
Please enter any 3rd number: 10
Largest number is: 30

"""
