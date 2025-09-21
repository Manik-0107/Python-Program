# Matrix is 2D List

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for col in row:
        print(col, end=" ")
    print()

print("\nIndex[2][0] = ",matrix[2][0])
matrix[2][0] = 1
print("\nIndex[2][0] = ",matrix[2][0])

for row in matrix:
    for col in row:
        print(col, end=" ")
    print()


print()

"""
1 2 3 
4 5 6 
7 8 9 

Index[2][0] =  7

Index[2][0] =  1
1 2 3 
4 5 6 
1 8 9 
"""
