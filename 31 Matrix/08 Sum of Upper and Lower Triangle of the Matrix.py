# Sum of the upper and lower triangle of the matrix

rn = int(input("\nPlease enter any row number for the matrix: "))
A = []

# Taking elements from the user for the matrix
print(f"Please enter {rn*rn} elements for the matrix---")
for row in range(rn):
    rows=[]
    for col in range(rn):
        value = int(input(f"A[{row+1}][{col+1}]: "))
        rows.append(value)
    A.append(rows)

# Print The Matrix
print("\nA: ", end=" ")
for row in range(rn):
    print("\t", end=" ")
    for col in range(rn):
        print(A[row][col], end=" ")
    print()

upper_sum = 0
lower_sum = 0

for row in range(rn):
    for col in range(rn):
        if row < col:
            upper_sum += A[row][col]
        if row > col:
            lower_sum += A[row][col]

print("\nSum of Upper Triangle value: ", upper_sum)
print("Sum of Lower Triangle value: ", lower_sum,"\n")

"""
Please enter any row number for the matrix: 3
Please enter 9 elements for the matrix---
A[1][1]: 1
A[1][2]: 2
A[1][3]: 3
A[2][1]: 4
A[2][2]: 5
A[2][3]: 6
A[3][1]: 7
A[3][2]: 8
A[3][3]: 9

A:       1 2 3 
         4 5 6 
         7 8 9 

Sum of Upper Triangle value:  11
Sum of Lower Triangle value:  19 
"""
