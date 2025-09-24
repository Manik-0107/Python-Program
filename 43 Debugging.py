# When there is an error or problem in a program, finding and fixing those errors or problems is called debugging
# I am using a simple program for practice, Debugging.

def add(*numbers):
  sum = 0
  for num in numbers:
    sum += num
    return sum          # this is a bug, because you don't get the expected result 

print(add(10, 20))
