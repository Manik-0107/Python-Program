n = int(input("Please enter any number of rows: "))

for row in range(1, n+1):
    for col in range(1, row+1):
        print("*", end=" ")
    print()

for row in range(n-1, 0, -1):
    for col in range(1, row+1):
        print("*", end=" ")
    print()





"""

Please enter any number of rows: 5

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 


"""
