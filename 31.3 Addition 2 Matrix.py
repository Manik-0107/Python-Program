r = int(input("\nPlease enter no. of row for matrix: "))
c = int(input("Please enter no. of column for matrix: "))

A = []
B = []

print("\nPlese enter ",r*c,"elements for A matrix..")
for row in range(r):
    rows=[]
    for col in range(c):
        value = int(input(f"A[{row+1}][{col+1}]= "))
        rows.append(value)
    A.append(rows)

print(f"\nPlease enter {r*c} elements for B matrix--")
for row in range(r):
    rows=[]
    for col in range(c):
        value = int(input(f"B[{row+1}][{col+1}]= "))
        rows.append(value)
    B.append(rows)

print("\nA = ", end="")
for row in A:
    print("\t", end="")
    for col in row:
        print(col, end=" ")
    print()

print("\nB = ", end="")
for row in B:
    print("\t", end="")
    for col in row:
        print(col, end=" ")
    print()

# A + B
C = []
for row in range(r):
    rows=[]
    for col in range(c):
        rows.append(A[row][col] + B[row][col])
    C.append(rows)

print("\nA + B = ")
for row in C:
    print("\t", end="")
    for col in row:
        print(col, end=" ")
    print()

print("\nThe Program is Successfully executed....\n\n")

"""
Please enter no. of rows for matrix: 2
Please enter no. of column for matrix: 2

Please enter  4 elements for A matrix..
A[1][1]= 1
A[1][2]= 2
A[2][1]= 3
A[2][2]= 4

Please enter 4 elements for B matrix--
B[1][1]= 5
B[1][2]= 6
B[2][1]= 7
B[2][2]= 8

A =     1 2 
        3 4 

B =     5 6 
        7 8 

A + B = 
        6 8 
        10 12 

The Program is Successfully executed....

"""
