import numpy as np
from scipy import stats
import pandas as pd
'''
# Create a 1D array
arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))
print(arr.shape)
print(arr.ndim)

#Create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

print(arr2d)
print(type(arr2d))
print(arr2d.shape)
print(arr2d.ndim)

#Create arrays with random initialization
randarr = np.random.randint(0, 10, size=10)
print(randarr)

randarr2d = np.random.randint(0, 10, size=(4,5))
print(randarr2d)


#Create arrays with  defualt initialization
zeros = np.zeros(10)
print(zeros)

ones = np.ones(5)
print(ones)

#Print diagonal values of a matrix
matrix = np.random.randint(0, 10, size=(3,3))
print(matrix)
print(np.diagonal(matrix)) 

#Print first element
print(arr[0])
print(arr2d[0,0])

#Print last element
print(arr[-1])
print(arr2d[-1,-1])

#Print 2nd row 2nd element
print(arr2d[1,1])

#Print number of elements
print(arr.size)
print(arr2d.size)

#Determinant of a matrix
mat1 = np.random.randint(0, 10, size=(3,3))
print(mat1)
print(np.linalg.det(mat1))

#Addition of two matrices
mat2 = np.random.randint(0, 10, size=(3,3))
print(mat2)
print("mat1 + mat2 = ", mat1 + mat2)

#Multiplication of two matrices
print("mat1 * mat2 = ", np.dot(mat1, mat2))

#Subtraction of two matrices
print("mat1 - mat2 = ", mat1 - mat2)

#Division of two matrices
print("mat1 / mat2 = ", mat1 / mat2)

#Transpose of a matrix
print("Transpose of mat1 = ", mat1.T)

#Cross product of two matrices
print("Cross product of mat1 and mat2 = ", np.cross(mat1, mat2))

#Dot product of two matrices
print("Dot product of mat1 and mat2 = ", np.dot(mat1, mat2))

#Array with range values
range_arr = np.arange(10)
print(range_arr)

range_arr2d = np.arange(16).reshape(4,4)
print(range_arr2d)

#Reshape an array
print("Original Array:\n", np.arange(12))
print("Reshaped Array:\n", np.arange(12).reshape(3,4))

#Array stats
arr = np.random.randint(0, 10, size=10)
print(arr)
print("Min: ", np.min(arr))
print("Max: ", np.max(arr))
print("Mean: ", np.mean(arr))
print("Median: ", np.median(arr))
print("Mode: ", stats.mode(arr))
print("Standard Deviation: ", np.std(arr))

#Create a mask for an array
arr = np.random.randint(0, 10, size=10)
print(arr)
mask = arr>5
print(mask)
filtered_arr = arr[mask]
print(filtered_arr)

#Fancy Indexing
arr = np.random.randint(0, 10, size=10)
print(arr)
indices = [1, 3, 5, 7, 9]
print(arr[indices])

#Structured array
dtype = [('name', 'U20'), ('age', 'i4'), ('grade', 'f4')]

students = np.array([('Alice', 20, 88.5),
                     ('Bob', 22, 92.0),
                     ('Charlie', 23, 85.0),
                     ('David', 21, 90.5),
                     ('Eva', 22, 89.0)],
                    dtype=dtype)
print(students['name'])
print(students['age'][3])
'''

#linear regression
df = pd.read_excel('dataset1.xlsx')

print(df)