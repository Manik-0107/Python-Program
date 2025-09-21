n = int(input("Enter row no.: "))

for row in range(n+1):
    for col in range(1, row+1):
        print(col*row, end=" ")
    print()

print()



"""

Enter row no.: 5

1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25 

"""
