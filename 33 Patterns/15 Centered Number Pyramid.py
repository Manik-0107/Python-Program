n = int(input("Please enter row no.: "))

for row in range(1, n+1):
    for col in range(n-row):
        print(" ", end=" ")
    for col in range(1, 2*row):
        print(col, end=" ")
    print()

print()



"""

Please enter row no.: 5

        1 
      1 2 3 
    1 2 3 4 5 
  1 2 3 4 5 6 7 
1 2 3 4 5 6 7 8 9 


"""
