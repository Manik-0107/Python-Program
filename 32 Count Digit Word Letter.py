numOfWord = 1
numOfLetter = 0
numOfDigit = 0

text = input("\nPlease enter text with number: ")

for i in text:
    if ('a'<=i<='z') or ('A'<=i<'Z'):
        numOfLetter += 1
    elif '0' <= i <= '9':
        numOfDigit += 1
    elif i == " ":
        numOfWord += 1

print("\nNumber of Digit: ", numOfDigit)
print("Number of Letters: ", numOfLetter)
print("Number of Words: ", numOfWord,"\n")




"""
Please enter text with number: My name is Manik Mondal and My username is Manik0107

Number of Digit:  4
Number of Letters:  39
Number of Words:  10 

"""
