# Cross Shape
n = int(input("\nEnter row no.: "))
print()
for row in range(n):
    for col in range(n):
        if col==row or row+col==n-1:
            print("*", end=" ")
        else:
            print(end="  ")
    print()
print()




"""

Enter row no.: 5

*       * 
  *   *   
    *     
  *   *   
*       * 


"""
