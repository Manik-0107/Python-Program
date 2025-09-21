n1 = int(input("Please enter any 1st number: "))
n2 = int(input("Please enter any 2nd number: "))
n3 = int(input("Please enter any 3rd number: "))

if n1 > n2:
    if n1 > n3:
        print(f"\nNumber {n1} is the Maximum number.")
    else:
        print(f"\nNumber {n3} is the Maximum number.")

else:
    if n2 > n3:
        print(f"\nNumber {n2} is the Maximum number.")
    
    else:
        print(f"\nNumber {n3} is the Maximum number.")

print()



"""
Please enter any 1st number: 40
Please enter any 2nd number: 10
Please enter any 3rd number: 50

Number 50 is the Maximum number.

"""
