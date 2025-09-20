rn = int(input("\nPlease enter any row number for the matrix: "))

A = []

# Taking elements from the user
print(f"\nPlease enter {rn*rn} elements for the matrix---")
for row in range(rn):
    rows = []
    for col in range(rn):
        value = int(input(f"A[{row+1}][{col+1}]: "))
        rows.append(value)
    A.append(rows)

# Print the Matrix
print("\nA: ", end=" ")
for row in range(rn):
    print("\t", end=" ")
    for col in range(rn):
        print(A[row][col], end=" ")
    print()

dig_sum = 0
for i in range(rn):
    dig_sum += A[i][i]
print("\nSum of diagonal elements: ", dig_sum)


print("\nGreat job 🎉✅ The program is executed successfully 🚀 \n")

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

Sum of diagonal elements:  15

Great job 🎉✅ The program is executed successfully 🚀 
"""
