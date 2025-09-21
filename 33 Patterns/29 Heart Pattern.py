n = int(input("\nEnter row no.: "))
print()
for row in range(1, 2*n):
    if row==2*n//4 or row==(2*n//2)+3:
        print("*", end=" ")
    else:
        print(end="  ")
print()

for row in range(1, 2*n):
    if (row>1 and row<5) or (row>7 and row<11):
        print("*", end=" ")
    else:
        print(end="  ")
print()

for row in range(1, n*2):
    if row==n*2//2:
        print(end="  ")
    else:
        print("*", end=" ")
print()

for row in range(n, 0, -1):
    for col in range(n-row):
        print(end="  ")
    for col in range(1, 2*row):
        print("*", end=" ")
    print()

print()





"""
Enter row no.: 6

    *           *     
  * * *       * * *   
* * * * *   * * * * * 
* * * * * * * * * * * 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 


"""
