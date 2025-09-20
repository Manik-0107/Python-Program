rn = int(input("\nPlease enter any row numbers: "))
cn = int(input("Please enter any column number: "))

matrix = []

print("\nPlease enter ",rn*cn," elements for matrix")
for row in range(rn):
    rows = []
    for col in range(cn):
        value = int(input(f"A[{row+1}][{col+1}] = "))
        rows.append(value)
    matrix.append(rows)
    print()

print("\nA = ", end=" ")
for row in matrix:
    print("\t", end=" ")
    for col in row:
        print(col, end=" ")
    print()

print()

# Please enter any row numbers: 3
# Please enter any column number: 3

# Please enter  9  elements for matrix
# A[1][1] = 1
# A[1][2] = 2
# A[1][3] = 3

# A[2][1] = 4
# A[2][2] = 5
# A[2][3] = 6

# A[3][1] = 7
# A[3][2] = 8
# A[3][3] = 9


# A =      1 2 3 
#          4 5 6 
#          7 8 9 
