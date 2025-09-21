n = int(input("\nEnter row no.: "))
print()
for row in range(n):
    print(" "*(n-row), end=" ")
    value = 1

    for col in range(row+1):
        print(value, end=" ")
        value = value*(row-col)//(col+1)
    print()
print()



"""
Enter row no.: 6

       1 
      1 1 
     1 2 1 
    1 3 3 1 
   1 4 6 4 1 
  1 5 10 10 5 1 


"""
