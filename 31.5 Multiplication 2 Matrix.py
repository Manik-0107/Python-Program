r1 = int(input("\nPlease enter any row no. for A matrix: "))
c1 = int(input("Please enter any column no. for A matrix: "))

r2 = int(input("\nPlease enter any row no. for B matrix: "))
c2 = int(input("Please enter any column no. for B matrix: "))

while c1 != r2:
    print("\nError..!!! Column of 1st matrix not equal to row of 2nd matrix..")
    r1 = int(input("\nPlease enter any row no. for A matrix: "))
    c1 = int(input("Please enter any column no. for A matrix: "))

    r2 = int(input("\nPlease enter any row no. for B matrix: "))
    c2 = int(input("Please enter any column no. for B matrix: "))

A = []
B = []

# Taking elements from user for A matrix
print(f"\nPlease enter {r1*c1} elements for A matrix----")
for row in range(r1):
    rows = []
    for col in range(c1):
        value = int(input(f"A[{row+1}][{col+1}]: "))
        rows.append(value)
    A.append(rows)

# Taking elements from user for B matrix
print(f"\nPlease enter {r2*c2} elements for B matrix---")
for row in range(r2):
    rows = []
    for col in range(c2):
        value = int(input(f"B[{row+1}][{col+1}]: "))
        rows.append(value)
    B.append(rows)

# Print A matrix
print("\nA = ", end=" ")
for row in A:
    print("\t", end=" ")
    for col in row:
        print(col, end=" ")
    print()

# Print B matrix
print("\nB = ", end=" ")
for row in B:
    print("\t", end=" ")
    for col in row:
        print(col, end=" ")
    print()

C = []
for row in range(r1):
    rows = []
    for col in range(c2):
        sum = 0
        for i in range(c1):
            sum += A[row][i] * B[i][col]
        rows.append(sum)
    C.append(rows)

print("\nA x B = ")
for row in C:
    print("\t", end=" ")
    for col in row:
        print(col, end=" ")
    print()

print("\nProgram is executed successfully....")
