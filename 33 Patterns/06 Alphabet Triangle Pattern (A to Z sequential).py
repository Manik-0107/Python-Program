n = int(input("Please enter any row number: "))

# for row in range(1, n+1):
#     for col in range(65, row+65):
#         print(chr(col), end=" ")
#     print()

for row in range(n):
    for col in range(row+1):
        print(chr(row+65), end=" ")
    print()




"""

Please enter any row number: 5

A 
B B 
C C C 
D D D D 
E E E E E 

"""
