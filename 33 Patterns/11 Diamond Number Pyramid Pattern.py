n = int(input("Please enter any number of rows: "))

for row in range(n+1):
    for col in range(n-row):
        print(" ", end=" ")
    for col in range(1, row+1):
        print(col, end=" ")
    print()

for row in range(n-1, 0, -1):
    for col in range(n-row):
        print(" ", end=" ")
    for col in range(1, row+1):
        print(col, end=" ")
    print()

print()



"""

Please enter any number of rows: 5

        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 
  1 2 3 4 
    1 2 3 
      1 2 
        1 

"""
