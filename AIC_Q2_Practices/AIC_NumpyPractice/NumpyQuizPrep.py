# # Numpy Quiz Preparation

# %%
print('*' * 10, 'Cell# 01', '*' * 10)
from os import pathsep, sep
import numpy as np

arr1 = np.random.randn(3, 4)  # creates a 2-d array with random signed number
arr2 = (np.absolute(arr1 * 2)).astype('i2')  # convertes the generated array to binary array.
print(arr1)
print(arr2)
print("\u001b[32m")
print("Mathematical Operations with ndarrays")

# vectorize Multiplication
print(arr2 * arr2)
# %%
print('*' * 10, 'Cell# 02', '*' * 10)
import numpy as np

# np.array() method is the simplest way to create ndarray
np_arr = np.array(())
np_asarr = np.asarray(np_arr)
np_empt = np.empty((2, 5))
np_arr1 = np.arange(21)
print("np_arr:", np_arr)
print('np_asarr', np_asarr)
print('np_arr1', np_arr1)
print(np_empt)
np_arrfl = np.full_like(np_asarr, 10, order='F')
print("Arr_Full", np_arrfl)
np_eye = np.eye(3, dtype=bool)
print("Eye", np_eye, sep='\n')
np_arr.data
# %%
print('*' * 10, 'Strides', '*' * 10)
import numpy as np

arr_md = np.array(np.arange(60), dtype='i2').reshape(12, 5)
print("4d-array", arr_md)
print("Dimensions", arr_md.ndim)
# Strides is a tuple contains
# for 2-d array (bytes step to next row,bytes step to next column)
# for n-d array (boyte step to next block,....,bytes step to next column)
ints_dtype = arr_md.dtype
print("array type:", ints_dtype)
print("array size:", arr_md.size)
print("array shape:", arr_md.shape)
# There are total 60 elements in this 2-d array with 12 rows and 5 cols
# each element occupies two bytes of memory therefore strides of this array will be (10,2), which means 2 bytes leap must be taken for next column and (5*2) 10 bytes jump for next row in the memoryself.
print("Array Strides:", arr_md.strides)
# There are two main superset fo np data types 1.) np.Integer, 2.)np.floating
print(np.issubdtype(ints_dtype, np.integer))
# %%
# # Numpy Quiz Preparation

# %%
print('*' * 10, 'Cell# 01', '*' * 10)
import numpy as np

arr1 = np.random.randn(3, 4)  # creates a 2-d array with random signed number
arr2 = (np.absolute(arr1 * 2)).astype('i2')  # convertes the generated array to binary array.
print(arr1)
print(arr2)
print("\u001b[32m")
print("Mathematical Operations with ndarrays")

# vectorize Multiplication
print(arr2 * arr2)
# %%
print('*' * 10, 'Cell# 02', '*' * 10)
import numpy as np

# np.array() method is the simplest way to create ndarray
np_arr = np.array(())
np_asarr = np.asarray(np_arr)
np_empt = np.empty((2, 5))
np_arr1 = np.arange(21)
print("np_arr:", np_arr)
print('np_asarr', np_asarr)
print('np_arr1', np_arr1)
print(np_empt)
np_arrfl = np.full_like(np_asarr, 10, order='F')
print("Arr_Full", np_arrfl)
np_eye = np.eye(3, dtype=bool)
print("Eye", np_eye, sep='\n')
np_arr.data
# %%
print('*' * 10, 'Strides', '*' * 10)
import numpy as np

arr_md = np.array(np.arange(60), dtype='i2').reshape(12, 5)
print("4d-array", arr_md)
print("Dimensions", arr_md.ndim)
# Strides is a tuple contains
# for 2-d array (bytes step to next row,bytes step to next column)
# for n-d array (boyte step to next block,....,bytes step to next column)
ints_dtype = arr_md.dtype
print("array type:", ints_dtype)
print("array size:", arr_md.size)
print("array shape:", arr_md.shape)
# There are total 60 elements in this 2-d array with 12 rows and 5 cols
# each element occupies two bytes of memory therefore strides of this array will be (10,2), which means 2 bytes leap must be taken for next column and (5*2) 10 bytes jump for next row in the memoryself.
print("Array Strides:", arr_md.strides)
# There are two main superset fo np data types 1.) np.Integer, 2.)np.floating
print(np.issubdtype(ints_dtype, np.integer))
# %%
# # Numpy Quiz Preparation

# %%
print('*' * 10, 'Cell# 01', '*' * 10)
import numpy as np

arr1 = np.random.randn(3, 4)  # creates a 2-d array with random signed number
arr2 = (np.absolute(arr1 * 2)).astype('i2')  # convertes the generated array to binary array.
print(arr1)
print(arr2)
print("\u001b[32m")
print("Mathematical Operations with ndarrays")

# vectorize Multiplication
print(arr2 * arr2)
# %%
print('*' * 10, 'Cell# 02', '*' * 10)
import numpy as np

# np.array() method is the simplest way to create ndarray
np_arr = np.array(())
np_asarr = np.asarray(np_arr)
np_empt = np.empty((2, 5))
np_arr1 = np.arange(21)
print("np_arr:", np_arr)
print('np_asarr', np_asarr)
print('np_arr1', np_arr1)
print(np_empt)
np_arrfl = np.full_like(np_asarr, 10, order='F')
print("Arr_Full", np_arrfl)
np_eye = np.eye(3, dtype=bool)
print("Eye", np_eye, sep='\n')
# %%
print('*' * 10, 'Strides', '*' * 10)
import numpy as np

arr_md = np.array(np.arange(60), dtype='i2').reshape(12, 5)
print("4d-array", arr_md)
print("Dimensions", arr_md.ndim)
# Strides is a tuple contains
# for 2-d array (bytes step to next row,bytes step to next column)
# for n-d array (boyte step to next block,....,bytes step to next column)
ints_dtype = arr_md.dtype
print("array type:", ints_dtype)
print("array size:", arr_md.size)
print("array shape:", arr_md.shape)
# There are total 60 elements in this 2-d array with 12 rows and 5 cols
# each element occupies two bytes of memory therefore strides of this array will be (10,2), which means 2 bytes leap must be taken for next column and (5*2) 10 bytes jump for next row in the memoryself.
print("Array Strides:", arr_md.strides)
# There are two main superset fo np data types 1.) np.Integer, 2.)np.floating
print(np.issubdtype(ints_dtype, np.integer))
# %%
# # Numpy Quiz Preparation

# %%
print('*' * 10, 'Cell# 01', '*' * 10)
import numpy as np

arr1 = np.random.randn(3, 4)  # creates a 2-d array with random signed number
arr2 = (np.absolute(arr1 * 2)).astype('i2')  # convertes the generated array to binary array.
print(arr1)
print(arr2)
print("\u001b[32m")
print("Mathematical Operations with ndarrays")

# vectorize Multiplication
print(arr2 * arr2)
# %%
import numpy as np

print('*' * 10, 'Cell# 02', '*' * 10)
# np.array() method is the simplest way to create ndarray
np_arr = np.array(())
np_asarr = np.asarray(np_arr)
np_empt = np.empty((2, 5))
np_arr1 = np.arange(21)
print("np_arr:", np_arr)
print('np_asarr', np_asarr)
print('np_arr1', np_arr1)
print(np_empt)
np_arrfl = np.full_like(np_asarr, 10, order='F')
print("Arr_Full", np_arrfl)
np_eye = np.eye(3, dtype=bool)
print("Eye", np_eye, sep='\n')
# %%
print('*' * 10, 'Strides', '*' * 10)
import numpy as np

arr_md = np.array(np.arange(60), dtype='i2').reshape(12, 5)
print("4d-array", arr_md)
print("Dimensions", arr_md.ndim)
# Strides is a tuple contains
# for 2-d array (bytes step to next row,bytes step to next column)
# for n-d array (boyte step to next block,....,bytes step to next column)
ints_dtype = arr_md.dtype
print("array type:", ints_dtype)
print("array size:", arr_md.size)
print("array shape:", arr_md.shape)
# There are total 60 elements in this 2-d array with 12 rows and 5 cols
# each element occupies two bytes of memory therefore strides of this array will be (10,2), which means 2 bytes leap must be taken for next column and (5*2) 10 bytes jump for next row in the memoryself.
print("Array Strides:", arr_md.strides)
# There are two main superset fo np data types 1.) np.Integer, 2.)np.floating
print(np.issubdtype(ints_dtype, np.integer))
print(np.floating.mro())  # This returns all the parent data type of the given data type in numpy

# %%
import numpy as np

print("*" * 10, "Apendix A.2")
# Flattening is the process to convert a higher dim numpy array to 1-d arrayself.
apdx_2d = np.ones((2, 3, 2), dtype='i2')
print("Higher-d array:", apdx_2d, sep='\n')
ravel_apdx_2d = apdx_2d.ravel()
print("3d to 1d:", ravel_apdx_2d)
print("3d strides:", apdx_2d.strides)

# Ravel mathod creates a view of the give array instead of creating a copy, here is the doemonstration
# ravel_apdx_2d[2:8] = np.array()
print("Updated Ravel:", ravel_apdx_2d, sep='\n')
print("Higher-d array:", apdx_2d, sep='\n')
# On the other hand flatten() method creates a copy of higher order array as 1-d array
flatten_apdx = apdx_2d.flatten()

# %%
end = 16
np_shape = (2, 2, 2, 2)
apdx_with_C_order = np.array(range(0, end)).reshape(np_shape)
apdx_with_F_order = np.array(range(0, end), order='F').reshape(np_shape)
apdx_with_K_order = np.array(range(0, end), order='K').reshape(np_shape)
print("apdx_with_C_order", apdx_with_C_order, sep='\n')
# print("apdx_with_F_order",apdx_with_F_order,sep='\n')
# print("apdx_with_K_order",apdx_with_K_order,sep='\n')
c_order_flatt = apdx_with_C_order.flatten()
f_order_flatt = apdx_with_F_order.ravel('F')
print("c_order_flat", c_order_flatt)
print("f_order_flat", f_order_flatt)

# %%
zero_axis_concat = np.concatenate((apdx_with_C_order, apdx_with_F_order), axis=2)
print("Zero Axis", zero_axis_concat, sep='\n')
print(zero_axis_concat.shape)
h_stack = np.hstack((apdx_with_C_order, apdx_with_F_order))
print("hstack", h_stack.shape)
# %%
print("*" * 10, "Splitting", '*' * 10)
one_d = np.arange(10)
print("One_d:", one_d, sep='\n')
splitted_arrs = np.split(one_d, 2)
splitted_arrs1 = np.split(one_d, [5, 7])
# print(splitted_arrs)
print(splitted_arrs1)
print(splitted_arrs1[2])

# %%
two_d = np.arange(1, 17).reshape(2, 2, 4)
print('*' * 10, 'Two_array Splitting', '*' * 10)
# Split over 3rd dimension, on index 1,2,3
split_two_d = np.split(two_d, [1, 2, 3], axis=2)
print("two_d:", two_d, sep='\n')

print("split_two_d:", len(split_two_d), sep='\n')
print("split_two_d[0]:", split_two_d[0], sep='\n')
print("split_two_d[1]:", split_two_d[1], sep='\n')
print("split_two_d[2]:", split_two_d[2], sep='\n')
print("split_two_d[3]:", split_two_d[3], sep='\n')

# %%
print('*' * 10, 'Repeating/Tiling', '*' * 10)
rpt_1d = np.arange(4)
rpt_2d = np.arange(8).reshape(2, 4)
# (axis 0)tiles 2 times-->(axis 1)tiles 3 times---> (axis 2)tiles 3 times
tiled_3d = np.tile(rpt_1d, [2, 3, 3])
print("tiling ", tiled_3d)
print(rpt_1d.size)
print(rpt_2d)
rptd = np.repeat(rpt_2d, [1, 3], axis=0)
print("rpted", rptd)

# %%
import array as ar

a = np.random.randn(2, 3)
print(a.data)

# %%
dic = {"A": 52, "b": 63, "c": 52}
np_arr = np.array(dic)
print(np_arr.dtype)
# %%
import numpy as np

w = np.full((2, 4), [[3, 5, 6, 5], [6, 5, 7, 8]], dtype='U1')
print(w.shape)
np
# %%
