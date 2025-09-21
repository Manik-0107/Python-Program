# Create a simple calculator that runs until the user chooses to exit (while loop).

while True:
    print("\nSimple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Existing calculator, Goodbye...")
        break

    num1 = float(input("Please enter any first number: "))
    num2 = float(input("Please enter any second number: "))

    if choice == "1":
        print("Addition value is: ", num1 + num2)
    elif choice == "2":
        print("Subtraction value is: ", num1-num2)
    elif choice == "3":
        print("Multiplication value is: ", num1*num2)
    elif choice == "4":
        if num2 != 0:
            print("Division value is: ", num1/num2)
        else:
            print("Error. Division by zero is not allowed !")
    else:
        print("Invalid choice. Please try again later.")







"""
Simple Calculator
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Enter your choice (1-5): 3
Please enter any first number: 10
Please enter any second number: 20
Multiplication value is:  200.0

Simple Calculator
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Enter your choice (1-5): 5
Existing calculator, Goodbye...
PS E:\Python\Python Practice> 


"""
