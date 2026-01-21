import numpy as np

arr = np.array([10,20,30,40,50])
print(arr)

print(arr[0:3])
print(arr[1:])
print(arr[0:])
print(arr[2:])
print(arr[:2])

print("\n\n\n")
arr = np.array([[10,20,30,40,50],[60,70,80,90,100]])
print(arr)
print(arr[0:2,0:2])
print(arr[0:2,0:3]) # Prints 3 as it follow same order
print(arr[0,1:3])
print(arr[1,3:])

print("\n\n\n")
arr = np.array([[10,20,30,40,50],[60,70,80,90,100],[30,40,50,60,70]])
print(arr)
print(arr[1,2])