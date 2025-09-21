# Upper half pyramid using natural numbers

n = int(input("Please enter row no.: "))

for row in range(n+1):
    for col in range(n-row):
        print(end=" ")
    for col in range(1, row+1):
        print(col, end=" ")
    print()

print()




"""

Please enter row no.: 5
     
    1 
   1 2 
  1 2 3 
 1 2 3 4 
1 2 3 4 5 


"""
