# Floyd's Triangle

n = int(input("\nEnter row no.: "))
count = 0
print()
for row in range(1, n+1):
    for col in range(1, row+1):
        count += 1
        print(count, end=" ")
    print()

print()





"""


Enter row no.: 5

1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 

"""
