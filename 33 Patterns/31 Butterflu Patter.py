n = int(input("\nEnter row no.: "))
print()
print("*" * n)

row = (n // 2) - 1
while row > 0:
    print("*" * row + " " * (n - 2*row) + "*" * row)
    row -= 1

print("🦋\n")



"""

Enter row no.: 14

**************
******  ******
*****    *****
****      ****
***        ***
**          **
*            *
🦋


"""
