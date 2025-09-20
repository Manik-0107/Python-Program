rn = int(input("\nPlease enter any row number: "))
cn = int(input("Please enter any column number: "))

A = []
B = []

print(f"\nPleae enter {rn*cn} elements for A matrix--")
for row in range(rn):
    rows=[]
    for col in range(cn):
        value = int(input(f"A[{row+1}][{col+1}]: "))
        rows.append(value)
    A.append(rows)

print(f"\nPlease enter {rn*cn} elements for B matrix--")
for row in range(rn):
    rows = []
    for col in range(cn):
        value = int(input(f"B[{row+1}][{col+1}]: "))
        rows.append(value)
    B.append(rows)

print("\nA = ", end="")
for row in A:
    print("\t", end=" ")
    for col in row:
        print(col, end=" ")
    print()

print("\nB = ", end=" ")
for row in B:
    print("\t", end=" ")
    for col in row:
        print(col, end=" ")
    print()

# A + B
C = []
for row in range(rn):
    rows = []
    for col in range(cn):
        rows.append(A[row][col] - B[row][col])
    C.append(rows)

print("\nA + B = ")
for row in C:
    print("\t", end=" ")
    for col in row:
        print(col, end="  ")
    print()

print("\nThe program is successfully executed")

"""
Please enter any row number: 2
Please enter any column number: 2

Please enter 4 elements for A matrix--
A[1][1]: 9
A[1][2]: 8
A[2][1]: 7
A[2][2]: 6

Please enter 4 elements for B matrix--
B[1][1]: 5
B[1][2]: 4
B[2][1]: 3
B[2][2]: 2

A =      9 8 
         7 6 

B =      5 4 
         3 2 

A + B = 
         4  4  
         4  4  

The program is successfully executed

"""
