# Mirror Number Triangle (decreasing order per row)

n = int(input("Please enter any number of rows: "))

for row in range(1, n+1):
    for col in range(row, 0, -1):
        print(col, end=" ")
    print()





"""

Please enter any number of rows: 5

1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1 

"""
