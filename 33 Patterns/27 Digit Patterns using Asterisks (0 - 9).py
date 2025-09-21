n = int(input("\nPlease enter any digit (0 - 9): "))
print()
if n == 0:
    for row in range(1, 7):
        for col in range(1, 6):
            if row==1 or col==1 or row==6 or col==5:
                print("*", end=" ")
            else:
                print(end="  ")
        print()

elif n == 1:
    for row in range(1, 8):
        for col in range(1, 6):
            if col==4-row or col==3 or row==7:
                print("*", end=" ")
            else:
                print(end="  ")
        print()

elif n==2:
    for row in range(1, 8):
        for col in range(1, 5):
            if row==1 or row==4 or row==7 or (col==4 and row <=4) or (col==1 and row >=4):
                print("*", end=" ")
            else:
                print(end="  ")
        print()

elif n==3:
    for row in range(1, 8):
        for col in range(1, 4):
            if row==1 or row==7 or row==4 or col==3:
                print("*", end=" ")
            else:
                print(end="  ")
        print()

elif n==4:
    for row in range(1, 8):
        for col in range(1, 7):
            if col==5 or row==5 or row+col==6:
                print("*", end=" ")
            else:
                print(end="  ")
        print()

elif n==5:
    for row in range(1, 8):
        for col in range(1, 6):
            if row==1 or row==4 or row==7 or (col==1 and row<=4) or (col==5 and row>=4):
                print("*", end=" ")
            else:
                print(end="  ")
        print()

elif n==6:
    for row in range(1, 8):
        for col in range(1, 6):
            if col==1 or row==1 or row==7 or row==4 or (col==5 and row>=4):
                print("*", end=" ")
            else:
                print(end="  ")
        print()

elif n==7:
    for row in range(1, 6):
        for col in range(1, 6):
            if row==1 or row+col==6:
                print("*", end=" ")
            else:
                print(end="  ")
        print()

elif n==8:
    for row in range(1, 8):
        for col in range(1, 6):
            if row==1 or row==4 or row==7 or col==1 or col==5:
                print("*", end=" ")
            else:
                print(end="  ")
        print()

elif n==9:
    for row in range(1, 8):
        for col in range(1, 6):
            if row==1 or row==4 or row==7 or col==5 or (col==1 and row<=4):
                print("*", end=" ")
            else:
                print(end="  ")
        print()
else:
    print(n,"is not a Valid digit.!!!")
    print("Please try again later...")
print()







"""

Please enter any digit (0 - 9): 7

* * * * * 
      *   
    *     
  *
*




Please enter any digit (0 - 9): 5

* * * * *
*
*
* * * * *
        *
        *
* * * * *


"""
