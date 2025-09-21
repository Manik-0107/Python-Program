mark = int(input("Please enter your mark: "))

if  80 <= mark <= 100:
    print("Grade: A+")
elif 70 <= mark <= 79:
    print("Grade: A")
elif 60 <= mark <= 69:
    print("Grade: -A")
elif 50 <= mark <= 59:
    print("Grade: B")
elif 40 <= mark <= 49:
    print("Grade: C")
elif 33 <= mark <= 39:
    print("Grade: D")
elif 0 <= mark < 33:
    print("Grade: F")
    print("You are fail !!!")
    print("Try again later...")
else:
    print("Invalid mark")




"""
Please enter your mark: 85
Grade: A+

"""
