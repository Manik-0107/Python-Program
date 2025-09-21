# Keep asking for marks input until the user enters a negative number, then print the average.

total = 0
count = 0
while True:
    mark = int(input("Please enter your positive mark: "))
    if mark > 0:
        # print(mark)
        total += mark
        count += 1
    else:
        break
print("\nToltal number is: ", total)
if count > 0:
    print("Avarage value is: ", total/count,"\n")
else:
    print("\nNo marks were entered")





"""
Please enter your positive mark: 54
Please enter your positive mark: 60
Please enter your positive mark: 80
Please enter your positive mark: 14
Please enter your positive mark: -9

Toltal number is:  208
Avarage value is:  52.0 

"""
