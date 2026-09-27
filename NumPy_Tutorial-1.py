import numpy as np
array=np.array([[2,4,6,8],
                [3,6,9,12],
                [4,8,12,16],
                [5,10,15,20]])
# array[start:end:step]

# # for row selection 
# print(array[0])
# print(array[0:4])
# print(array[0:4:-1])
# print(array[4::-1])
# print(array[0,0:2]) 

# # for column selection  
# print(array[:,1])
# print(array[:,-1])
# print(array[:,0:3])

# Scalar Arithmetic
new_Array=[1.01,2,3.5,4]
# print(new_Array + 2)
# this will result in an error as this is a normal list

new_Array=np.array(new_Array)
print(new_Array+ 2)
print(new_Array ** 5)

# Vectorised math functions
print(np.sqrt(new_Array))
print(np.floor(new_Array))
print(np.ceil(new_Array))
print(np.pi * new_Array **2)

# Element Wise Arithmetic
arr1=np.array([1,2,3])
arr2=np.array([2,3,4])
print(arr1+arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)
print(arr1 ** arr2)

# Comparision Operators

scores=np.array([90,55,100,75,82,89])
print(scores == 100)
scores[scores<60]=0
print(scores)

 

