n = int(input("Enter row no.: "))
print()
for row in range(n):
    for col in range(n):
        if row==n-1 or col==0 or row==col:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()




"""

Enter row no.: 5

*
* *       
*   *     
*     *   
* * * * * 


"""
