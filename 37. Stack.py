books = []

# Store the book in the stack using .push() function
books.append("Learn C")
books.append("Learn C++")
books.append("Learn Java")

print("\n",books)

# Remove the book in the stack using .pop() function
books.pop()
print("Now The top book is: ", books[-1])

books.pop()
print("Now The top book is: ", books[-1])

books.pop()
if not books:
    print("Books not left")



"""

['Learn C', 'Learn C++', 'Learn Java']
Now, the top book is:  Learn C++
Now the top book is:  Learn C
Books not left

"""
