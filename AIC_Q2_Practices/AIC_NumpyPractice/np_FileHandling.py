import numpy as np

# Saves the given array to the file name as "Some Array" in first argument.
# np.save("Some Array",np.array(np.arange(30)).reshape(2,3,5))
# Loads the data from the file as ndarray
# print(np.load("Some Array.npy"))

# To save multiple arrays in a file. a file that contains multiple arrays
#  stores all arrays as dictionary data structure (key-value) pair.
np.savez("moreArrays.npz", a=np.array(np.arange(30)).reshape((2, 3, 5)), b=np.array(np.arange(20)).reshape(4, 5))
arr_ld = np.load("moreArrays.npz")
print(arr_ld.pop)
