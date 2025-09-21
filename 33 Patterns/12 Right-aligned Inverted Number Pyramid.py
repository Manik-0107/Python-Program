n = int(input("Please enter any number of row: "))

for row in range(n, 0, -1):
    for col in range(n-row):
        print(" ", end=" ")
    for col in range(1, row+1):
        print(col, end=" ")
    print()
print()



"""

Please enter any number of row: 5

1 2 3 4 5 
  1 2 3 4 
    1 2 3 
      1 2 
        1 

"""
