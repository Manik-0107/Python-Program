# Get the largest element of a list
def largest(arr, index=0):
    # Base case: if we reached the last element
    if index == len(arr) - 1:
        return arr[index]
    
    # Recursive step: compare current element with largest of rest
    return max(arr[index], largest(arr, index + 1))


n = int(input("Please enter how many elements: "))
A = []

for i in range(n):
    value = int(input(f"A[{i+1}]: "))
    A.append(value)

print(f"Largest element is: {largest(A)}")


"""
Please enter how many elements: 3
A[1]: 20
A[2]: 50
A[3]: 30
Largest element is: 50

"""
