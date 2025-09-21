# Right-Aligned Triangle Pattern

n = int(input("Please enter any row number: "))

for i in range(n+1):
    print(" " * (n-i) + "*"*i)



"""
Please enter any row number: 7
       
      *
     **
    ***
   ****
  *****
 ******
*******


"""
