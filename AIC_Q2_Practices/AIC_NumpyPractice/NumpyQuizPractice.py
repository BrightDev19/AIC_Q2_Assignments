
# %%
import numpy as n

arr = n.array([67.98,-10.25,-22.06,0.5,12.9,10.10])
print(arr.sort())
print(arr.astype(n.int32))
print(n.reshape(arr,(2,3)))
print(arr.reshape(2,3))
# %%
import numpy as np
a = np.array([0,1])
b = np.array([0,2])
print(np.row_stack((a,b)))
# %%
arr = np.arange(10)
arr_slice = arr[8:5]
# arr_slice[:] = 69
print(arr_slice)
lst = [5,6,2,4,8,6,8]
lst_slice = lst[-5:-1]
print(lst_slice)
# %%
names = ['Ali','Neha','Hamza','neha','Fatima','Hamza']
np_names = np.array(names)
print(np.unique(np_names))
# %%
a= np.arange(10).reshape(2,-1)
b= np.repeat(1,10).reshape(2,-1)
print(np.concatenate((a,b),axis=0))
print(np.vstack((a,b)))
print(np.r_[a,b])
a.sort()
# %%
a= np.array([[0,1,2,45],[3,4,5,7],[6,7,8,8]])
b= np.array([[0,2,4,47],[6,8,10,9],[12,14,16,7]])
print(np.dstack((a,b)))
# %%
