def list_Element(arr, index=0):
    if index >= len(arr):
        return
    print(arr[index], end=" ")
    list_Element(arr, index+1)


n = int(input("Please enter how many elements: "))
A = []

for i in range(n):
    value = int(input(f"A[{i+1}]: "))
    A.append(value)

print("Array elements: ", end=" ")
list_Element(A) 
print()




"""
Please enter how many elements: 6
A[1]: 1
A[2]: 5
A[3]: 3
A[4]: 6
A[5]: 9
A[6]: 4
Array elements:  1 5 3 6 9 4 

"""
