import numpy as np
# the foundational open-source library for numerical and scientific computing in Python. It introduces the ndarray (N-dimensional array), a fast, memory-efficient data structure that is up to 50x faster than traditional Python lists for processing datasets.
py_array=[1,2,3,4]
print(py_array)
print((py_array)*2)

# This is the speciality of numpy arrays which allows mathematical operations to be done on the array
array=np.array([1,2,3,4])
print(array)
print(type(array))
print((array)*2)

array0D=np.array('A')

array1D=np.array(['A','B','C'])

array2D=np.array([['A','B','C'],['C','D','E'],['F',np.nan,np.nan]])


array3D = np. array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                   [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])

print(array1D.ndim)
print(array2D.ndim)
print(array3D.ndim)
print(array0D.ndim)
print(array1D.shape)
print(array2D.shape)
print(array3D.shape)
print(array0D.shape)

# Chain Indexing
print(array3D[0][0][0])
# Multi-Dinmensional Indexing
print(array3D[0,0,0])
# Multi-dimensional indexing is way faster as comapared to chain indexing


#This is String Concatenation 
word=array3D[0,0,0]+array3D[1,0,0]+array3D[1,0,0]
print(word)