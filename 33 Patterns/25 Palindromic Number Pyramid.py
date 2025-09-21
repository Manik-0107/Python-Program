n = int(input("\nEnter row number: "))
print()
for row in range(1, n+1):
    for col in range(n-row):
        print(end="  ")
    for col in range(1, row+1):
        print(col, end=" ")
    for col in range(row-1, 0, -1):
        print(col, end=" ")
    print()
print()




"""

Enter row number: 5

        1 
      1 2 1 
    1 2 3 2 1 
  1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 


"""
