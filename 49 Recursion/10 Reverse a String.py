# Reverse a string using recursion

def reverse_string(str):
  if len(str) == 0:
    return str
  else:
    return reverse_string(str[1:] + str[0]

string = input("Please enter any string: ")
print("Reverse string is: ", reverse_string(string))


"""
Enter any string: Manik
Reverse string is:  kinaM

"""
