n = int(input("Please enter row no.: "))

for row in range(n+1):
    for col in range(n-row):
        print(" ", end=" ")
    for col in range(1, 2*row):
        print(col, end=" ")
    print()

for row in range(n-1, 0, -1):
    for col in range(n-row):
        print(" ", end=" ")
    for col in range(1, 2*row):
        print(col, end=" ")
    print()




"""

Please enter row no.: 5

        1 
      1 2 3 
    1 2 3 4 5 
  1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 9 
  1 2 3 4 5 6 7 
    1 2 3 4 5 
      1 2 3 
        1 


""""
