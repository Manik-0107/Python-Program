from collections import deque

# Store the data in the Queue
bank = deque(["Manik", "Rahul", "Surya"])
print("\n",bank)

bank.popleft()      # remove the data from queue using .popleft()
print(bank)

bank.popleft()
print(bank)

bank.popleft()
if not bank:
    print("The person is not left.")




"""

 deque(['Manik', 'Rahul', 'Surya'])
deque(['Rahul', 'Surya'])
deque(['Surya'])
The person is not left.

"""
