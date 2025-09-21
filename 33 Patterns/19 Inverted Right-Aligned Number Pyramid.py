n = int(input("Enter row no.: "))
print()
for row in range(n, 0, -1):
    for col in range(n-row):
        print(end=" ")
    for col in range(1, row+1):
        print(col, end=" ")
    print()
print()




"""

Enter row no.: 5

1 2 3 4 5 
 1 2 3 4 
  1 2 3 
   1 2 
    1 


"""
