import numpy as np

A = np.array([[1,1,1],[2,2,2],[3,3,3]])
B = np.array([[1,1,1],[2,2,2],[3,3,3]])
C = np.array([[1,1,1],[2,2,2],[3,3,3]])

result = A.dot(B).dot(C)
print("Multiplication of the matrix:")
print(result)
