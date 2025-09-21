rn = int(input("\nPlease enter any row number for the matrix: "))
cn = int(input("Please enter any column number for the matrix: "))

A = []

# Taking elements from the user
print(f"\nPlease enter {rn*cn} elements for the matrix: ")
for row in range(rn):
    rows = []
    for col in range(cn):
        value = int(input(f"A[{row+1}][{col+1}]: "))
        rows.append(value)
    A.append(rows)

# Print Matrix
print("\nA:  ", end=" ")
for row in A:
    print("\t", end=" ")
    for col in row:
        print(col, end=" ")
    print()

# Transpose Matrix
print("\nT: ", end=" ")
for row in range(cn):
    print("\t", end=" ")
    for col in range(rn):
        print(A[col][row], end=" ")
    print()

print("\nThe Program is successfully executed..\n")

"""
Please enter any row number for the matrix: 2
Please enter any column number for the matrix: 3

Please enter 6 elements for the matrix: 
A[1][1]: 1
A[1][2]: 2
A[1][3]: 3
A[2][1]: 4
A[2][2]: 5
A[2][3]: 6

A:       1 2 3 
         4 5 6 

T:       1 4 
         2 5 
         3 6 

The Program is successfully executed..
"""
