n = int(input("\nEnter row number: "))
print()

for row in range(n//2, n, 2):
    for col in range(1, n-row, 2):
        print(end="  ")
    for col in range(1, row+1):
        print("*", end=" ")
    for col in range(1, n-row+1):
        print(end="  ")
    for col in range(1, row+1):
        print("*", end=" ")
    print()

for row in range(n, 0, -1):
    for col in range(n-row):
        print(end="  ")
    for col in range(1, 2*row):
        print("*", end=" ")
    print()




"""

Enter row number: 6

  * * *       * * * 
* * * * *   * * * * * 
* * * * * * * * * * * 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 


"""
