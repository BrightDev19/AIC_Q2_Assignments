import numpy as np
import os

# Linear Algebra in Numpy
# Matrix multiplication
mat1 = np.array(np.arange(8).reshape((2, 4)))
mat2 = np.array(np.arange(8).reshape((2, 4)))
print("{0} x {1} \n= {2}".format(mat1, mat2, mat1 * mat2))

