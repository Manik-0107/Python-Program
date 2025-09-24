def naturalNo(i, n):
    if i <= n:
        print(i, end=" ")
        naturalNo(i+1, n)

num = int(input("Please enter the last number: "))
print("Natural Number: ", end=" ")
naturalNo(1, num)

# Return the value
print("\n\nReturn value from the function")
def natNo(i, n):
    if i > n:
        return []
    else:
        return [i] + natNo(i+1, n)
print("Natural numbers: ", natNo(1, num))
print()



"""
Please enter the last number: 7
Natural Number:  1 2 3 4 5 6 7 

Return value from the function
Natural numbers:  [1, 2, 3, 4, 5, 6, 7]

"""
