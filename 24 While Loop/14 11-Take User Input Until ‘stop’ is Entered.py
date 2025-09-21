# Keep taking input from the user until they enter “stop” (using while loop).

while True:
    user_input = input("Enter something (type 'stop' to end): ")
    if user_input.lower() == "stop":
        break
    print("You entered:", user_input)




"""
Enter something (type 'stop' to end): hi
You entered: hi
Enter something (type 'stop' to end): hello
You entered: hello
Enter something (type 'stop' to end): stop
PS E:\Python\Python Practice> 

"""
